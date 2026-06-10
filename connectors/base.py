# connectors/base.py

from abc import ABC, abstractmethod
from typing import BinaryIO, Dict, List, Optional
from models.document import Document


class BaseConnector(ABC):
    """
    Base class for all document connectors (Google Drive, S3, Local FS, etc.)
    """

    @abstractmethod
    def list_documents(self, **kwargs) -> List[Dict]:
        """
        Return list of available documents in the source.
        """
        raise NotImplementedError

    @abstractmethod
    def fetch_document(self, document_id: str) -> Document:
        """
        Fetch a single document and return standardized Document model.
        """
        raise NotImplementedError

    @abstractmethod
    def download_file(self, document_id: str) -> BinaryIO:
        """
        Download raw file stream.
        """
        raise NotImplementedError

    @abstractmethod
    def get_metadata(self, document_id: str) -> Dict:
        """
        Fetch metadata for a document.
        """
        raise NotImplementedError