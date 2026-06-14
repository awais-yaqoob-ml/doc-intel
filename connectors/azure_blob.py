# connectors/azure_blob.py

from datetime import datetime
from io import BytesIO
from typing import Any, BinaryIO, Dict, List, Optional

from .base import BaseConnector
from models.document import Document, DocumentMetadata
from utils.mime import get_mime_type


class AzureBlobConnector(BaseConnector):
    """
    Azure Blob Storage connector.

    Authenticates with a connection string (or account URL + credential)
    and exposes blobs as the internal :class:`Document` model.

    Notes
    -----
    The `azure-storage-blob` package is imported lazily so the rest of
    the project keeps working even when the dependency is not installed.
    Install it with::

        pip install azure-storage-blob>=12.20,<13.0
    """

    def __init__(
        self,
        connection_string: Optional[str] = None,
        account_url: Optional[str] = None,
        credential: Optional[Any] = None,
        container_name: Optional[str] = None,
        prefix: str = "",
    ) -> None:
        if not connection_string and not (account_url and credential):
            raise ValueError(
                "Provide either `connection_string` or both "
                "`account_url` and `credential`."
            )

        self.connection_string = connection_string
        self.account_url = account_url
        self.credential = credential
        self.container_name = container_name
        self.prefix = prefix

        self._service_client = self._authenticate()
        self._container_client = (
            self._service_client.get_container_client(container_name)
            if container_name
            else None
        )

    # ------------------------------------------------------------------ auth

    def _authenticate(self):
        """
        Build an authenticated `BlobServiceClient`.

        Uses the Azure Python SDK (`azure-storage-blob`).
        """
        try:
            from azure.storage.blob import BlobServiceClient  # type: ignore
        except ImportError as exc:  # pragma: no cover - import guard
            raise ImportError(
                "The `azure-storage-blob` package is required for "
                "AzureBlobConnector. Install it with: "
                "`pip install azure-storage-blob`."
            ) from exc

        if self.connection_string:
            return BlobServiceClient.from_connection_string(
                self.connection_string
            )

        return BlobServiceClient(
            account_url=self.account_url,
            credential=self.credential,
        )

    # ------------------------------------------------------------ container

    def _ensure_container_client(self, container_name: Optional[str] = None):
        """
        Resolve a container client, falling back to the default one set
        in the constructor.
        """
        target = container_name or self.container_name
        if not target:
            raise ValueError(
                "No container specified. Pass `container_name` to the "
                "method or set it on the connector instance."
            )
        if container_name and container_name != self.container_name:
            return self._service_client.get_container_client(target)
        if self._container_client is None:
            return self._service_client.get_container_client(target)
        return self._container_client

    # -------------------------------------------------------------- helpers

    @staticmethod
    def _infer_file_type(blob_name: str) -> str:
        """
        Best-effort file type extraction from a blob name.
        """
        if "." not in blob_name:
            return "unknown"
        return blob_name.rsplit(".", 1)[-1].lower()

    # ----------------------------------------------------------- Base API

    def list_documents(
        self,
        container_name: Optional[str] = None,
        prefix: Optional[str] = None,
        **kwargs,
    ) -> List[Dict]:
        """
        List blobs in a container as plain dictionaries.

        Parameters
        ----------
        container_name:
            Optional container override.
        prefix:
            Optional name prefix filter (defaults to ``self.prefix``).
        """
        container = self._ensure_container_client(container_name)
        effective_prefix = prefix if prefix is not None else self.prefix

        results: List[Dict] = []
        for blob in container.list_blobs(name_starts_with=effective_prefix):
            results.append(
                {
                    "id": blob.name,
                    "name": blob.name,
                    "mimeType": get_mime_type(blob.name),
                    "size_bytes": getattr(blob, "size", None),
                    "last_modified": getattr(
                        blob, "last_modified", None
                    ),
                    "content_type": getattr(
                        blob, "content_settings", None
                    ),
                    "container": container.container_name,
                }
            )
        return results

    def fetch_document(
        self,
        document_id: str,
        container_name: Optional[str] = None,
    ) -> Document:
        """
        Download a blob and convert it into the internal ``Document``
        model.
        """
        container = self._ensure_container_client(container_name)
        blob_client = container.get_blob_client(document_id)

        properties = blob_client.get_blob_properties()
        content_settings = getattr(properties, "content_settings", None)
        content_type = (
            getattr(content_settings, "content_type", None)
            if content_settings is not None
            else None
        )

        metadata = DocumentMetadata(
            filename=document_id,
            file_type=content_type
            or get_mime_type(document_id)
            or self._infer_file_type(document_id),
            size_bytes=getattr(properties, "size", 0) or 0,
            uploaded_at=getattr(properties, "last_modified", None)
            or datetime.utcnow(),
            source="azure_blob",
        )

        return Document(
            id=document_id,
            metadata=metadata,
            content=None,
            page_count=None,
        )

    def download_file(
        self,
        document_id: str,
        container_name: Optional[str] = None,
    ) -> BinaryIO:
        """
        Stream a blob's raw bytes into an in-memory buffer.
        """
        container = self._ensure_container_client(container_name)
        blob_client = container.get_blob_client(document_id)
        stream = blob_client.download_blob()
        return BytesIO(stream.readall())

    def get_metadata(
        self,
        document_id: str,
        container_name: Optional[str] = None,
    ) -> Dict:
        """
        Fetch blob properties (size, content type, etag, ...).
        """
        container = self._ensure_container_client(container_name)
        blob_client = container.get_blob_client(document_id)
        properties = blob_client.get_blob_properties()

        return {
            "id": document_id,
            "container": container.container_name,
            "source": "azure_blob",
            "size_bytes": getattr(properties, "size", None),
            "content_type": getattr(
                getattr(properties, "content_settings", None),
                "content_type",
                None,
            ),
            "etag": getattr(properties, "etag", None),
            "last_modified": getattr(properties, "last_modified", None),
        }
