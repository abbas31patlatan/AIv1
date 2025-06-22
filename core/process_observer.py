"""Observe and record process activity."""
from __future__ import annotations


class ProcessObserver:
    """Track processes in a very simple way."""

    def __init__(self) -> None:
        self.events: list[str] = []

    def record(self, event: str) -> None:
        self.events.append(event)
