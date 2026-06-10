# chunking/hierarchical.py

from typing import List, Dict, Any
from .base import BaseChunker


class HierarchicalChunker(BaseChunker):
    """
    Hierarchical chunking:
    paragraph -> section -> chunk
    """

    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def _split_paragraphs(self, text: str) -> List[str]:
        return [p.strip() for p in text.split("\n\n") if p.strip()]

    def _split_text(self, text: str) -> List[str]:
        chunks = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size
            chunks.append(text[start:end])
            start = end - self.overlap
        return chunks

    def chunk(self, text: str, **kwargs) -> List[Dict[str, Any]]:
        paragraphs = self._split_paragraphs(text)

        all_chunks: List[Dict[str, Any]] = []

        for i, para in enumerate(paragraphs):
            sub_chunks = self._split_text(para)

            for j, chunk in enumerate(sub_chunks):
                all_chunks.append(
                    {
                        "chunk_id": f"p{i}_c{j}",
                        "text": chunk,
                        "paragraph_index": i,
                        "chunk_index": j,
                    }
                )

        return all_chunks