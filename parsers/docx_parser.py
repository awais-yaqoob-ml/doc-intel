# parsers/docx_parser.py

from typing import Dict
from .base import BaseParser


class DocxParser(BaseParser):
    """
    DOCX parser (stub implementation).
    """

    def parse(self, file_path: str, **kwargs) -> Dict:
        return {
            "file_type": "docx",
            "content": "Sample DOCX text",
        }

    def parse_bytes(self, file_bytes: bytes, **kwargs) -> Dict:
        return self.parse("bytes_input", **kwargs)

    def supported_formats(self) -> list[str]:
        return ["docx"]