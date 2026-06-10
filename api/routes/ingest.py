# api/routes/ingest.py

from fastapi import APIRouter, UploadFile, File, Depends
from uuid import uuid4

from api.dependencies import get_orchestrator, get_job_tracker
from models.job import ProcessingJob, JobStatus

router = APIRouter()


@router.post("/ingest")
async def ingest(
    file: UploadFile = File(...),
    orchestrator=Depends(get_orchestrator),
    tracker=Depends(get_job_tracker),
):
    job_id = str(uuid4())
    document_id = str(uuid4())

    job = ProcessingJob(
        job_id=job_id,
        document_id=document_id,
        status=JobStatus.PENDING,
    )

    tracker.create_job(job)

    # NOTE: sync execution for now
    result = orchestrator.process(job)

    tracker.update_status(job_id, JobStatus.COMPLETED)

    return {
        "job_id": job_id,
        "document_id": document_id,
        "result": result,
    }