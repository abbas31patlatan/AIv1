"""Example feedback loop for iterative improvement."""
from __future__ import annotations


class FeedbackLoop:
    """Collect feedback strings and allow retrieval."""

    def __init__(self) -> None:
        self._feedback: list[str] = []

    def add(self, text: str) -> None:
        self._feedback.append(text)

    def all(self) -> list[str]:
        return list(self._feedback)
