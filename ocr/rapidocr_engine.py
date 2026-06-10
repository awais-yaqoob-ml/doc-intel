# ocr/rapidocr_engine.py

from typing import List
from .base import BaseOCREngine
from models.ocr import OCRResult, OCRPage, OCRTextLine
from datetime import datetime


class RapidOCREngine(BaseOCREngine):
    """
    RapidOCR-based engine (stub wrapper).
    Replace internal call with rapidocr-onnxruntime.
    """

    def __init__(self, use_gpu: bool = False):
        self.use_gpu = use_gpu
        self.model = self._load_model()

    def _load_model(self):
        # Placeholder for RapidOCR initialization
        return None

    def extract(self, file_path: str, **kwargs) -> OCRResult:
        # Stub implementation
        page = OCRPage(
            page_number=1,
            text_lines=[
                OCRTextLine(text="Sample extracted text", confidence=0.98)
            ],
        )

        return OCRResult(
            document_id=kwargs.get("document_id", "unknown"),
            pages=[page],
            full_text="Sample extracted text",
            mean_confidence=0.98,
        )

    def extract_from_bytes(self, file_bytes: bytes, **kwargs) -> OCRResult:
        return self.extract(file_path="bytes_input", **kwargs)

    def supported_formats(self) -> List[str]:
        return ["png", "jpg", "jpeg", "pdf"]