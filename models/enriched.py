# models/enriched.py

from pydantic import BaseModel, Field
from typing import List, Dict, Optional


class EnrichedSection(BaseModel):
    section_id: str
    text: str
    summary: Optional[str] = None
    entities: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)
    metadata: Dict = Field(default_factory=dict)


class EnrichedDocument(BaseModel):
    document_id: str
    sections: List[EnrichedSection] = Field(default_factory=list)
    global_summary: Optional[str] = None
    entities: List[str] = Field(default_factory=list)
    keywords: List[str] = Field(default_factory=list)