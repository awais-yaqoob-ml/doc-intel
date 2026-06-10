# api/main.py

from fastapi import FastAPI

from api.routes.health import router as health_router
from api.routes.ingest import router as ingest_router
from api.routes.search import router as search_router
from api.routes.extract import router as extract_router

app = FastAPI(title="OCR Document Intelligence API")

app.include_router(health_router, prefix="/api")
app.include_router(ingest_router, prefix="/api")
app.include_router(search_router, prefix="/api")
app.include_router(extract_router, prefix="/api")


@app.get("/")
def root():
    return {"message": "Document Intelligence System Running"}