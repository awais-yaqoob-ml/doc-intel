# models/metrics.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProcessingMetrics(BaseModel):
    document_id: str
    ocr_time_ms: Optional[float] = None
    extraction_time_ms: Optional[float] = None
    enrichment_time_ms: Optional[float] = None
    search_index_time_ms: Optional[float] = None
    total_time_ms: Optional[float] = None
    timestamp: datetime = datetime.utcnow()