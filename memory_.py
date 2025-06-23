"""In‑memory text storage with rudimentary retrieval facilities.

The :class:`Memory` class stores pieces of text and exposes a handful of
convenience methods to add, update and search those pieces using a trivial
Jaccard similarity.  While the implementation is intentionally lightweight it
serves to demonstrate how a memory component could be plugged into a larger
system.  The entries can also be persisted to JSON via :meth:`save` and later
restored with :meth:`load`.

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
from pathlib import Path
from typing import Dict, List, Tuple

from utils.json_handler import load_json, save_json


@dataclass
class MemoryEntry:
    """Represents a single memory record."""

    text: str
    tokens: Counter[str] = field(init=False)

    def __post_init__(self) -> None:
        self.tokens = Counter(self.text.lower().split())


class Memory:
    """Container for stored memory entries with optional autosave.

    Parameters
    ----------
    autosave_path:
        When provided the memory contents will be written to this path every
        time an entry is changed.  This keeps disk state in sync with memory at
        the cost of extra I/O.
    """

    def __init__(self, autosave_path: str | Path | None = None) -> None:
        self._entries: Dict[int, MemoryEntry] = {}
        self._next_id = 0
        self._autosave: Path | None = Path(autosave_path) if autosave_path else None

    def add(self, text: str) -> int:
        """Add a new memory entry and return its identifier."""
        entry = MemoryEntry(text)
        entry_id = self._next_id
        self._entries[entry_id] = entry
        self._next_id += 1
        self._maybe_autosave()
        return entry_id

    def get(self, entry_id: int) -> str:
        """Return the text for *entry_id* or raise ``KeyError``."""
        return self._entries[entry_id].text

    def update(self, entry_id: int, text: str) -> None:
        """Replace the text at *entry_id* with a new value."""
        self._entries[entry_id] = MemoryEntry(text)
        self._maybe_autosave()

    def remove(self, entry_id: int) -> None:
        """Delete the entry identified by *entry_id* if present."""
        self._entries.pop(entry_id, None)
        self._maybe_autosave()

    def clear(self) -> None:
        """Remove all stored entries."""
        self._entries.clear()
        self._next_id = 0
        self._maybe_autosave()

    # ------------------------------------------------------------------
    # Persistence helpers
    # ------------------------------------------------------------------

    def save(self, path: str | Path) -> None:
        """Serialise all entries to JSON at *path*."""
        data = {eid: entry.text for eid, entry in self._entries.items()}
        save_json(path, data)

    def load(self, path: str | Path) -> None:
        """Load entries from a JSON file."""
        data = load_json(path)
        self.clear()
        for text in data.values():
            self.add(text)

    def enable_autosave(self, path: str | Path) -> None:
        """Enable autosave to *path* for subsequent modifications."""
        self._autosave = Path(path)

    def search_regex(self, pattern: str) -> List[int]:
        """Return entry ids whose text matches the regex *pattern*."""
        import re

        regex = re.compile(pattern)
        return [eid for eid, entry in self._entries.items() if regex.search(entry.text)]

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

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _maybe_autosave(self) -> None:
        """Persist memory if autosave is enabled."""
        if self._autosave:
            self.save(self._autosave)
