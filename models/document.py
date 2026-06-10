# models/document.py

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class DocumentMetadata(BaseModel):
    filename: str
    file_type: str
    size_bytes: int
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
    source: Optional[str] = None


class Document(BaseModel):
    id: str
    metadata: DocumentMetadata
    content: Optional[str] = None
    page_count: Optional[int] = None
    tags: List[str] = Field(default_factory=list)