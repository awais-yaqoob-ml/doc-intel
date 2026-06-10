# parsers/router.py

from typing import Dict, Any, Optional
from .pdf_parser import PDFParser
from .docx_parser import DocxParser
from .image_parser import ImageParser


class ParserRouter:
    """
    Routes file parsing to the correct parser.
    """

    def __init__(self):
        self.parsers = {
            "pdf": PDFParser(),
            "docx": DocxParser(),
            "png": ImageParser(),
            "jpg": ImageParser(),
            "jpeg": ImageParser(),
        }

    def get_parser(self, file_extension: str):
        parser = self.parsers.get(file_extension.lower())
        if not parser:
            raise ValueError(f"No parser found for: {file_extension}")
        return parser

    def parse(self, file_path: str, file_extension: str, **kwargs) -> Dict[str, Any]:
        parser = self.get_parser(file_extension)
        return parser.parse(file_path, **kwargs)

    def parse_bytes(self, file_bytes: bytes, file_extension: str, **kwargs) -> Dict[str, Any]:
        parser = self.get_parser(file_extension)
        return parser.parse_bytes(file_bytes, **kwargs)