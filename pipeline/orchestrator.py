# pipeline/orchestrator.py

from typing import Dict, Any
from models.job import ProcessingJob

from parsers.router import ParserRouter
from ocr.rapidocr_engine import RapidOCREngine
from chunking.hierarchical import HierarchicalChunker
from embedding.embedder import Embedder
from storage.vector_store import InMemoryVectorStore
from storage.metadata_store import InMemoryMetadataStore
from enrichment.ner import NERExtractor
from enrichment.classifier import DocumentClassifier


class Orchestrator:
    """
    End-to-end document intelligence pipeline coordinator.
    """

    def __init__(self):
        self.parser = ParserRouter()
        self.ocr = RapidOCREngine()
        self.chunker = HierarchicalChunker()
        self.embedder = Embedder()

        self.vector_store = InMemoryVectorStore()
        self.metadata_store = InMemoryMetadataStore()

        self.ner = NERExtractor()
        self.classifier = DocumentClassifier()

    def process(self, job: ProcessingJob) -> Dict[str, Any]:
        """
        Full pipeline execution:
        parse -> ocr -> chunk -> embed -> enrich -> store
        """

        document_id = job.document_id

        # 1. Parse (stub: assume pdf)
        parsed = self.parser.parse(document_id, "pdf")

        # 2. OCR fallback (simplified)
        ocr_result = self.ocr.extract(file_path=document_id, document_id=document_id)

        text = ocr_result.full_text or ""

        # 3. Chunking
        chunks = self.chunker.chunk(text)

        # 4. Embeddings
        embeddings = self.embedder.embed([c["text"] for c in chunks])

        vector_items = []
        for chunk, emb in zip(chunks, embeddings):
            vector_items.append(
                {
                    "id": chunk["chunk_id"],
                    "embedding": emb.tolist(),
                    "metadata": chunk,
                    "document_id": document_id,
                }
            )

        self.vector_store.upsert(vector_items)

        # 5. Enrichment
        entities = self.ner.extract(text)
        classification = self.classifier.classify(text)

        # 6. Metadata store
        self.metadata_store.save(
            document_id,
            {
                "entities": entities,
                "classification": classification,
                "num_chunks": len(chunks),
            },
        )

        return {
            "document_id": document_id,
            "chunks": len(chunks),
            "entities": len(entities),
            "classification": classification,
        }