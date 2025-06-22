"""Aggregate logs from various sources."""
from __future__ import annotations


class LogCollector:
    """Store strings representing log entries."""

    def __init__(self) -> None:
        self.logs: list[str] = []

    def add(self, entry: str) -> None:
        self.logs.append(entry)
