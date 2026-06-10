# parsers/pdf_parser.py

from typing import Dict, Any, List
from .base import BaseParser


class PDFParser(BaseParser):
    """
    PDF parser (stub implementation).
    Extend with PyMuPDF / pdfplumber later.
    """

    def parse(self, file_path: str, **kwargs) -> Dict[str, Any]:
        return {
            "file_type": "pdf",
            "pages": [
                {"page_number": 1, "text": "Sample PDF text"}
            ],
        }

    def parse_bytes(self, file_bytes: bytes, **kwargs) -> Dict[str, Any]:
        return self.parse("bytes_input", **kwargs)

    def supported_formats(self) -> list[str]:
        return ["pdf"]