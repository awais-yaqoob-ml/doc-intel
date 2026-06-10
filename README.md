# Document Intelligence System (OCR + Enrichment + RAG Pipeline)

A modular end-to-end document intelligence system that supports:

- Document ingestion (API + connectors)
- OCR processing (RapidOCR-based engine)
- Parsing (PDF, DOCX, Images)
- Chunking (hierarchical strategy)
- Embedding generation
- Vector search (in-memory store)
- Metadata + metrics tracking
- NLP enrichment (NER, classification, OpenIE)
- FastAPI backend
- Streamlit dashboard

---
## Architecture Overview

Pipeline flow:

```

Upload / Connector
↓
Parser
↓
OCR
↓
Chunking
↓
Embedding
↓
Vector Store + Metadata Store
↓
Enrichment (NER / Classifier / OpenIE)
↓
Search API

```

---

## Project Structure

```

models/          → Data models (Pydantic schemas)
connectors/      → External data sources (Google Drive, etc.)
ocr/             → OCR engines + layout detection
parsers/         → File format parsers
chunking/        → Text chunking strategies
embedding/       → Embedding generation
storage/         → Vector + metadata + raw storage
enrichment/      → NLP enrichment modules
pipeline/        → Orchestration + job system
api/             → FastAPI backend
utils/           → Shared utilities
dashboard/       → Streamlit UI

````

---

## Quick Start

### 1. Install dependencies

```bash
uv pip install -e .
````

---

### 2. Run API

```bash
uvicorn api.main:app --reload
```

API will be available at:

```
http://localhost:8000
# You can access swagger docs at
http://localhost:8000/docs
```

---

### 3. Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

## API Endpoints

### Health

```
GET /api/health
```

### Ingest Document

```
POST /api/ingest
```

### Search

```
POST /api/search
```

### Extract Entities

```
POST /api/extract
```

---

## Key Design Features

### 1. Modular Architecture

Each component is independent:

* OCR engine swappable
* Parser router extensible
* Storage layer abstracted

### 2. Pluggable Storage

Supports:

* In-memory vector store (default)
* Extensible to Weaviate / FAISS / Pinecone

### 3. Pipeline Orchestration

Central orchestrator manages:

* parsing
* OCR
* chunking
* embedding
* enrichment

### 4. Async-Ready Design

Utilities prepared for async scaling.

---

## TO DO

### Production upgrades:

* Replace in-memory vector store with Weaviate / FAISS
* Add Redis queue for job runner
* Add proper async job execution (Celery / RQ)
* Add authentication layer
* Add document versioning

### Model upgrades:

* Replace stub OCR with full RapidOCR pipeline
* Add transformer-based NER (spaCy / HF)
* Add LLM-based summarization
* Add reranking for search

---

## Example Use Case

1. Upload PDF
2. System extracts text via OCR
3. Text is chunked
4. Embeddings generated
5. Stored in vector DB
6. User queries via semantic search
7. Enriched results returned (entities, classification)

---

## License

Internal / Experimental POC

---
