# chunking/base.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any


class BaseChunker(ABC):
    """
    Base interface for text chunking strategies.
    """

    @abstractmethod
    def chunk(self, text: str, **kwargs) -> List[Dict[str, Any]]:
        """
        Split text into chunks.
        """
        raise NotImplementedError