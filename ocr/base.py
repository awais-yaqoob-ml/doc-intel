# ocr/base.py

from abc import ABC, abstractmethod
from typing import Any, Dict, List
from models.ocr import OCRResult


class BaseOCREngine(ABC):
    """
    Abstract OCR engine interface.
    """

    @abstractmethod
    def extract(self, file_path: str, **kwargs) -> OCRResult:
        """
        Run OCR on a file and return structured OCRResult.
        """
        raise NotImplementedError

    @abstractmethod
    def extract_from_bytes(self, file_bytes: bytes, **kwargs) -> OCRResult:
        """
        Run OCR directly on file bytes.
        """
        raise NotImplementedError

    @abstractmethod
    def supported_formats(self) -> List[str]:
        """
        Return supported file formats (e.g. ["png", "jpg", "pdf"]).
        """
        raise NotImplementedError