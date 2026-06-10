# parsers/image_parser.py

from typing import Dict
from .base import BaseParser


class ImageParser(BaseParser):
    """
    Image parser (OCR-backed in real pipeline).
    """

    def parse(self, file_path: str, **kwargs) -> Dict:
        return {
            "file_type": "image",
            "content": "OCR text placeholder",
        }

    def parse_bytes(self, file_bytes: bytes, **kwargs) -> Dict:
        return self.parse("bytes_input", **kwargs)

    def supported_formats(self) -> list[str]:
        return ["png", "jpg", "jpeg", "tiff"]