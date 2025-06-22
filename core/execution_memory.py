"""History of executed actions."""
from __future__ import annotations


class ExecutionMemory:
    """Keep a list of performed actions."""

    def __init__(self) -> None:
        self.actions: list[str] = []

    def add(self, action: str) -> None:
        self.actions.append(action)

    def recent(self, limit: int = 5) -> list[str]:
        return self.actions[-limit:]
