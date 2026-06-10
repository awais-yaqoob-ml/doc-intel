# storage/base_metadata_store.py

from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List


class BaseMetadataStore(ABC):
    """
    Stores structured metadata (documents, jobs, metrics, etc.)
    """

    @abstractmethod
    def save(self, key: str, value: Dict[str, Any]) -> None:
        """
        Save metadata entry.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve metadata by key.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, key: str) -> bool:
        """
        Delete metadata entry.
        """
        raise NotImplementedError

    @abstractmethod
    def list(self, prefix: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        List metadata entries.
        """
        raise NotImplementedError