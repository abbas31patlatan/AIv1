"""Track session identifiers."""
from __future__ import annotations


class SessionManager:
    """Generate incremental session ids."""

    def __init__(self) -> None:
        self._next = 0

    def new_session(self) -> int:
        self._next += 1
        return self._next
