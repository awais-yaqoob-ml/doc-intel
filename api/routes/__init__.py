# api/routes/__init__.py

from .health import router as health_router
from .ingest import router as ingest_router
from .search import router as search_router
from .extract import router as extract_router

__all__ = [
    "health_router",
    "ingest_router",
    "search_router",
    "extract_router",
]