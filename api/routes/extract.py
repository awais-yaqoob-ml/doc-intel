# api/routes/extract.py

from fastapi import APIRouter, Depends
from api.dependencies import get_orchestrator

router = APIRouter()


@router.post("/extract")
def extract(document_id: str, orchestrator=Depends(get_orchestrator)):
    # Placeholder extraction endpoint
    return {
        "document_id": document_id,
        "entities": [],
        "message": "Extraction stub - integrate enrichment pipeline",
    }