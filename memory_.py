"""Simple in-memory storage with text retrieval.

The :class:`Memory` class stores text entries and allows searching using a very
basic Jaccard similarity over token sets. This is merely illustrative and not
suitable for production AI workloads.
"""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass
class MemoryEntry:
    """Represents a single memory record."""

    text: str
    tokens: Counter[str] = field(init=False)

    def __post_init__(self) -> None:
        self.tokens = Counter(self.text.lower().split())


class Memory:
    """Container for stored memory entries."""

    def __init__(self) -> None:
        self._entries: Dict[int, MemoryEntry] = {}
        self._next_id = 0

    def add(self, text: str) -> int:
        """Add a new memory entry and return its identifier."""
        entry = MemoryEntry(text)
        entry_id = self._next_id
        self._entries[entry_id] = entry
        self._next_id += 1
        return entry_id

    def search(self, query: str, limit: int = 3) -> List[Tuple[int, float]]:
        """Return entry ids sorted by similarity to the query."""
        query_tokens = Counter(query.lower().split())
        scores = []
        for entry_id, entry in self._entries.items():
            score = self._jaccard(query_tokens, entry.tokens)
            scores.append((entry_id, score))
        return sorted(scores, key=lambda s: s[1], reverse=True)[:limit]

    @staticmethod
    def _jaccard(a: Counter[str], b: Counter[str]) -> float:
        intersection = sum((a & b).values())
        union = sum((a | b).values())
        return intersection / union if union else 0.0
