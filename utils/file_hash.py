# utils/file_hash.py

import hashlib
from typing import Union


def sha256_file(file_bytes: Union[bytes, bytearray]) -> str:
    """
    Compute SHA-256 hash of file bytes.
    """
    sha = hashlib.sha256()
    sha.update(file_bytes)
    return sha.hexdigest()


def sha256_text(text: str) -> str:
    """
    Compute SHA-256 hash of text.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()