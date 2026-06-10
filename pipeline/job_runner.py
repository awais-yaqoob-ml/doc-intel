# pipeline/job_runner.py

from typing import Dict, Any
from models.job import ProcessingJob, JobStatus


class JobRunner:
    """
    Executes a single processing job.
    """

    def __init__(self, orchestrator):
        self.orchestrator = orchestrator

    def run(self, job: ProcessingJob) -> Dict[str, Any]:
        """
        Run full pipeline for a job.
        """
        job.status = JobStatus.RUNNING

        try:
            result = self.orchestrator.process(job)
            job.status = JobStatus.COMPLETED
            return result

        except Exception as e:
            job.status = JobStatus.FAILED
            job.error = str(e)
            raise