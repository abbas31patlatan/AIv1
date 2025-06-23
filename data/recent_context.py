"""Maintain a buffer of recent conversation snippets."""
from __future__ import annotations

from collections import deque
from typing import Deque


class RecentContext:
    """Store a limited number of text snippets."""

    def __init__(self, limit: int = 10) -> None:
        self.entries: Deque[str] = deque(maxlen=limit)

    def add(self, text: str) -> None:
        self.entries.append(text)

    def get(self) -> list[str]:
        return list(self.entries)
