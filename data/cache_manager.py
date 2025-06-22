"""Tiny in-memory cache with size limit."""
from __future__ import annotations

from collections import OrderedDict


class CacheManager:
    """Simple LRU cache implementation."""

    def __init__(self, limit: int = 128) -> None:
        self.limit = limit
        self._cache: OrderedDict[str, str] = OrderedDict()

    def get(self, key: str) -> str | None:
        value = self._cache.pop(key, None)
        if value is not None:
            self._cache[key] = value
        return value

    def set(self, key: str, value: str) -> None:
        if key in self._cache:
            self._cache.pop(key)
        elif len(self._cache) >= self.limit:
            self._cache.popitem(last=False)
        self._cache[key] = value
