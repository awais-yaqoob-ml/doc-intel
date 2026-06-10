# storage/metadata_store.py

from typing import Dict, Any, Optional, List
from .base_metadata_store import BaseMetadataStore


class InMemoryMetadataStore(BaseMetadataStore):
    """
    Simple in-memory metadata store.
    """

    def __init__(self):
        self.store: Dict[str, Dict[str, Any]] = {}

    def save(self, key: str, value: Dict[str, Any]) -> None:
        self.store[key] = value

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        return self.store.get(key)

    def delete(self, key: str) -> bool:
        if key in self.store:
            del self.store[key]
            return True
        return False

    def list(self, prefix: Optional[str] = None) -> List[Dict[str, Any]]:
        items = []
        for k, v in self.store.items():
            if prefix and not k.startswith(prefix):
                continue
            items.append({"key": k, "value": v})
        return items