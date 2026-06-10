# storage/base_raw_store.py

from abc import ABC, abstractmethod
from typing import BinaryIO, Dict, Optional


class BaseRawStore(ABC):
    """
    Stores raw files (PDFs, images, DOCX, etc.)
    """

    @abstractmethod
    def save(self, file_id: str, data: BinaryIO, metadata: Optional[Dict] = None) -> str:
        """
        Save raw file and return storage path/key.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, file_id: str) -> BinaryIO:
        """
        Load raw file by ID.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, file_id: str) -> bool:
        """
        Delete raw file.
        """
        raise NotImplementedError