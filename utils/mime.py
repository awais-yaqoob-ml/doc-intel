# utils/mime.py

import mimetypes
from typing import Optional


def get_mime_type(filename: str) -> Optional[str]:
    """
    Detect MIME type from filename.
    """
    mime, _ = mimetypes.guess_type(filename)
    return mime


def is_supported_file(filename: str, supported: list[str]) -> bool:
    """
    Check if file extension is supported.
    """
    ext = filename.lower().split(".")[-1]
    return ext in supported