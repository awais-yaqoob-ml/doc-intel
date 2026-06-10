# models/extraction.py

from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class ExtractedChunk(BaseModel):
    chunk_id: str
    text: str
    page_number: Optional[int] = None
    confidence: Optional[float] = None
    metadata: Dict = Field(default_factory=dict)


class ExtractionResult(BaseModel):
    document_id: str
    chunks: List[ExtractedChunk] = Field(default_factory=list)
    total_chunks: int = 0
    language: Optional[str] = None