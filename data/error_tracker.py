"""Collect runtime errors for later inspection."""
from __future__ import annotations


class ErrorTracker:
    """Simple list-based error tracker."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def add(self, message: str) -> None:
        self.errors.append(message)
