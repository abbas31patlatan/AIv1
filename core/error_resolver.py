"""Collect and provide simple error reports."""
from __future__ import annotations


class ErrorResolver:
    """Store errors and provide last error details."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def record(self, message: str) -> None:
        self.errors.append(message)

    def last_error(self) -> str | None:
        return self.errors[-1] if self.errors else None
