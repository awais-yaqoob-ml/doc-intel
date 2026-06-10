# storage/base_vector_store.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional


class BaseVectorStore(ABC):
    """
    Stores embeddings for semantic search.
    """

    @abstractmethod
    def upsert(
        self,
        items: List[Dict[str, Any]],
        namespace: Optional[str] = None,
    ) -> None:
        """
        Insert or update vectors.
        Each item should contain id, embedding, and metadata.
        """
        raise NotImplementedError

    @abstractmethod
    def query(
        self,
        vector: List[float],
        top_k: int = 5,
        namespace: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Query nearest neighbors.
        """
        raise NotImplementedError