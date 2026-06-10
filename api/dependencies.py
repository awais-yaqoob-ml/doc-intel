# api/dependencies.py

from pipeline.orchestrator import Orchestrator
from pipeline.job_tracker import JobTracker
from pipeline.job_runner import JobRunner


def get_orchestrator() -> Orchestrator:
    return Orchestrator()


def get_job_tracker() -> JobTracker:
    return JobTracker()


def get_job_runner(orchestrator: Orchestrator) -> JobRunner:
    return JobRunner(orchestrator=orchestrator)