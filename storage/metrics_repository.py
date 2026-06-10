# storage/metrics_repository.py

from typing import Dict, Any, List
from datetime import datetime


class MetricsRepository:
    """
    Stores processing metrics in-memory (stub).
    """

    def __init__(self):
        self.metrics: List[Dict[str, Any]] = []

    def record(self, metric: Dict[str, Any]) -> None:
        metric = {
            **metric,
            "timestamp": metric.get("timestamp", datetime.utcnow()),
        }
        self.metrics.append(metric)

    def get_all(self) -> List[Dict[str, Any]]:
        return self.metrics

    def get_by_document(self, document_id: str) -> List[Dict[str, Any]]:
        return [m for m in self.metrics if m.get("document_id") == document_id]