# pipeline/job_tracker.py

from typing import Dict, Optional
from datetime import datetime
from models.job import ProcessingJob, JobStatus


class JobTracker:
    """
    Tracks lifecycle of processing jobs.
    """

    def __init__(self):
        self.jobs: Dict[str, ProcessingJob] = {}

    def create_job(self, job: ProcessingJob) -> ProcessingJob:
        self.jobs[job.job_id] = job
        return job

    def get_job(self, job_id: str) -> Optional[ProcessingJob]:
        return self.jobs.get(job_id)

    def update_status(self, job_id: str, status: JobStatus, error: str = None) -> None:
        job = self.jobs.get(job_id)
        if not job:
            raise KeyError(f"Job not found: {job_id}")

        job.status = status
        job.updated_at = datetime.utcnow()

        if error:
            job.error = error