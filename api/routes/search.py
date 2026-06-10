# api/routes/search.py

from fastapi import APIRouter, Depends

from api.dependencies import get_orchestrator

router = APIRouter()


@router.post("/search")
def search(query: str, orchestrator=Depends(get_orchestrator)):
    # Placeholder: vector search would be exposed via orchestrator stores
    return {
        "query": query,
        "results": [],
        "message": "Search endpoint stub - connect vector store query",
    }