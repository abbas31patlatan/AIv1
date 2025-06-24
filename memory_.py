"""In‑memory text storage with rudimentary retrieval facilities.

The :class:`Memory` class stores pieces of text and exposes a handful of
convenience methods to add, update and search those pieces using a trivial
Jaccard similarity.  While the implementation is intentionally lightweight it
serves to demonstrate how a memory component could be plugged into a larger
system.

Example
-------
>>> m = Memory()
>>> ident = m.add("hello world")
>>> m.search("hello")
[(ident, 1.0)]
>>> m.update(ident, "goodbye world")
>>> len(m)
1
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

    def get(self, entry_id: int) -> str:
        """Return the text for *entry_id* or raise ``KeyError``."""
        return self._entries[entry_id].text

    def update(self, entry_id: int, text: str) -> None:
        """Replace the text at *entry_id* with a new value."""
        self._entries[entry_id] = MemoryEntry(text)

    def remove(self, entry_id: int) -> None:
        """Delete the entry identified by *entry_id* if present."""
        self._entries.pop(entry_id, None)

    def clear(self) -> None:
        """Remove all stored entries."""
        self._entries.clear()
        self._next_id = 0

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

    def __len__(self) -> int:
        """Return the number of stored entries."""
        return len(self._entries)

    def __iter__(self):
        """Iterate over stored entry texts in insertion order."""
        for entry_id in sorted(self._entries):
            yield self._entries[entry_id].text
