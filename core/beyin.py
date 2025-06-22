"""Simple brain simulation storing short-term thoughts."""
from __future__ import annotations

from collections import deque
from typing import Deque


class Beyin:
    """Maintain a small rolling buffer of thoughts."""

    def __init__(self, capacity: int = 5) -> None:
        self.thoughts: Deque[str] = deque(maxlen=capacity)

    def think(self, thought: str) -> None:
        self.thoughts.append(thought)

    def recall(self) -> list[str]:
        return list(self.thoughts)
