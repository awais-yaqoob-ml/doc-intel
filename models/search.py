# models/search.py

from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class SearchQuery(BaseModel):
    query: str
    top_k: int = 5
    filters: Dict = Field(default_factory=dict)


class SearchHit(BaseModel):
    doc_id: str
    chunk_id: Optional[str] = None
    score: float
    text: str


class SearchResult(BaseModel):
    query: str
    hits: List[SearchHit] = Field(default_factory=list)