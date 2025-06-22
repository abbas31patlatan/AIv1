"""Event analytics utilities.

This module provides a small :class:`EventTracker` used for counting
application events. It is intentionally lightweight to avoid external
dependencies but demonstrates how analytics could be integrated.

Example
-------
>>> tracker = EventTracker()
>>> tracker.log_event('login')
>>> tracker.counts['login']
1
"""
from __future__ import annotations

from collections import Counter
from typing import Iterable


class EventTracker:
    """Track simple event counts."""

    def __init__(self) -> None:
        self.counts: Counter[str] = Counter()

    def log_event(self, name: str) -> None:
        """Record a single *name* event."""
        self.counts[name] += 1

    def merge(self, events: Iterable[str]) -> None:
        """Merge a batch of event names."""
        self.counts.update(events)
