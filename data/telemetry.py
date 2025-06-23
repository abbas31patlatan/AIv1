"""Collect telemetry metrics."""
from __future__ import annotations


class Telemetry:
    """Store key-value metrics."""

    def __init__(self) -> None:
        self.metrics: dict[str, int] = {}

    def increment(self, name: str) -> None:
        self.metrics[name] = self.metrics.get(name, 0) + 1
