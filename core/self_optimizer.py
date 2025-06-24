"""Self optimisation routines."""
from __future__ import annotations


class SelfOptimizer:
    """Keep track of configuration tweaks."""

    def __init__(self) -> None:
        self.history: list[str] = []

    def apply(self, change: str) -> None:
        self.history.append(change)
