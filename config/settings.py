from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # Application
    app_name: str = "doc-intel"
    app_env: str = "local"
    debug: bool = False
    log_level: str = "INFO"

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    # PostgreSQL
    postgres_host: str
    postgres_port: int = 5432
    postgres_db: str
    postgres_user: str
    postgres_password: str

    # Qdrant
    qdrant_host: str
    qdrant_port: int = 6333
    qdrant_collection: str = "document_chunks"

    # Storage
    raw_storage_path: Path = Path("./data/raw")

    # Embeddings
    embedding_model: str = "BAAI/bge-small-en-v1.5"
    embedding_batch_size: int = 32

    # OCR
    ocr_engine: str = "rapidocr"
    ocr_max_concurrency: int = 2

    # Parsing
    parser_max_concurrency: int = 4

    # NER
    ner_model: str = "urchade/gliner_medium-v2.1"

    # Groq
    groq_api_key: str = Field(default="")
    groq_model: str = "llama-3.3-70b-versatile"
    groq_max_retries: int = 5
    groq_timeout_seconds: int = 120
    groq_max_concurrency: int = 3

    # Chunking
    chunk_size: int = 1024
    chunk_overlap: int = 128

    # Pipeline
    max_document_concurrency: int = 5

    # Google Drive
    google_drive_folder_id: str = ""
    google_service_account_file: str = (
        "credentials/google-service-account.json"
    )

    # Azure Blob Storage
    azure_blob_connection_string: str = ""
    azure_blob_account_url: str = ""
    azure_blob_container_name: str = ""
    azure_blob_prefix: str = ""

    @property
    def postgres_url(self) -> str:
        """Build async PostgreSQL connection URL."""

        return (
            f"postgresql+asyncpg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}"
            f"/{self.postgres_db}"
        )

    @property
    def qdrant_url(self) -> str:
        """Build Qdrant URL."""

        return (
            f"http://{self.qdrant_host}:{self.qdrant_port}"
        )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return singleton settings instance."""

    return Settings()


settings = get_settings()