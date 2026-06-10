# connectors/google_drive.py

from typing import BinaryIO, Dict, List
from .base import BaseConnector
from models.document import Document, DocumentMetadata
from datetime import datetime


class GoogleDriveConnector(BaseConnector):
    """
    Google Drive connector (stub implementation).
    Replace with real Google Drive API client later.
    """

    def __init__(self, credentials: Dict):
        self.credentials = credentials
        self.client = self._authenticate()

    def _authenticate(self):
        # Placeholder for Google Drive API authentication
        return None

    def list_documents(self, **kwargs) -> List[Dict]:
        """
        List files in Google Drive.
        """
        return [
            {
                "id": "file_1",
                "name": "sample.pdf",
                "mimeType": "application/pdf",
            }
        ]

    def fetch_document(self, document_id: str) -> Document:
        """
        Convert Drive file into internal Document model.
        """
        metadata = DocumentMetadata(
            filename="sample.pdf",
            file_type="pdf",
            size_bytes=1024,
            uploaded_at=datetime.utcnow(),
            source="google_drive",
        )

        return Document(
            id=document_id,
            metadata=metadata,
            content=None,
            page_count=None,
        )

    def download_file(self, document_id: str) -> BinaryIO:
        """
        Download raw file (stub).
        """
        from io import BytesIO
        return BytesIO(b"dummy file content")

    def get_metadata(self, document_id: str) -> Dict:
        """
        Fetch metadata (stub).
        """
        return {
            "id": document_id,
            "source": "google_drive",
            "status": "stub",
        }