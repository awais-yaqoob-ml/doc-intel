# models/ocr.py

from pydantic import BaseModel, Field
from typing import List, Optional


class OCRBox(BaseModel):
    x1: float
    y1: float
    x2: float
    y2: float


class OCRTextLine(BaseModel):
    text: str
    confidence: float
    bbox: Optional[OCRBox] = None


class OCRPage(BaseModel):
    page_number: int
    text_lines: List[OCRTextLine] = Field(default_factory=list)


class OCRResult(BaseModel):
    document_id: str
    pages: List[OCRPage] = Field(default_factory=list)
    full_text: Optional[str] = None
    mean_confidence: Optional[float] = None