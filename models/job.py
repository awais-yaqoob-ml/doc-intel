# models/job.py

from pydantic import BaseModel
from typing import Optional, Dict
from enum import Enum
from datetime import datetime


class JobStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class ProcessingJob(BaseModel):
    job_id: str
    document_id: str
    status: JobStatus = JobStatus.PENDING
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()
    error: Optional[str] = None
    context: Dict = {}