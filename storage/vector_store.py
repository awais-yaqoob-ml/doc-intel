# storage/vector_store.py

from typing import List, Dict, Any, Optional
import numpy as np
from .base_vector_store import BaseVectorStore


class InMemoryVectorStore(BaseVectorStore):
    """
    Simple in-memory vector store using cosine similarity (stub).
    """

    def __init__(self):
        self.vectors: List[Dict[str, Any]] = []

    def upsert(
        self,
        items: List[Dict[str, Any]],
        namespace: Optional[str] = None,
    ) -> None:
        for item in items:
            self.vectors.append(item)

    def _cosine(self, a: np.ndarray, b: np.ndarray) -> float:
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8))

    def query(
        self,
        vector: List[float],
        top_k: int = 5,
        namespace: Optional[str] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        query_vec = np.array(vector)

        scored = []
        for item in self.vectors:
            score = self._cosine(query_vec, np.array(item["embedding"]))
            scored.append({**item, "score": score})

        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:top_k]