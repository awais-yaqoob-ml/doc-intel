# embedding/embedder.py

from typing import List, Optional, Union
import numpy as np


class Embedder:
    """
    Embedding interface wrapper (stub).
    Replace with OpenAI / sentence-transformers / local embedding model.
    """

    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = self._load_model()

    def _load_model(self):
        """
        Placeholder model loader.
        """
        return None

    def embed(self, text: Union[str, List[str]]) -> np.ndarray:
        """
        Generate embeddings for text or list of texts.
        Returns numpy array of shape:
        - (dim,) for single string
        - (n, dim) for list of strings
        """
        if isinstance(text, str):
            return self._fake_vector(text)

        return np.array([self._fake_vector(t) for t in text])

    def _fake_vector(self, text: str, dim: int = 384) -> np.ndarray:
        """
        Deterministic pseudo-embedding (stub for dev/testing).
        """
        seed = abs(hash(text)) % (2**32)
        rng = np.random.default_rng(seed)
        return rng.random(dim).astype(np.float32)