# storage/raw_store.py

from typing import BinaryIO, Dict, Optional
from .base_raw_store import BaseRawStore


class LocalRawStore(BaseRawStore):
    """
    Simple local filesystem-based raw file store (stub).
    """

    def __init__(self, base_path: str = "/tmp/raw_store"):
        self.base_path = base_path
        self._store: Dict[str, bytes] = {}

    def save(self, file_id: str, data: BinaryIO, metadata: Optional[Dict] = None) -> str:
        content = data.read()
        self._store[file_id] = content
        return f"{self.base_path}/{file_id}"

    def load(self, file_id: str) -> BinaryIO:
        from io import BytesIO

        if file_id not in self._store:
            raise KeyError(f"File not found: {file_id}")

        return BytesIO(self._store[file_id])

    def delete(self, file_id: str) -> bool:
        if file_id in self._store:
            del self._store[file_id]
            return True
        return False