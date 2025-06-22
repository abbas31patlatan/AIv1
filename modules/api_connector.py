"""Generic API connector using :mod:`requests` (mocked)."""
from __future__ import annotations


class APIConnector:
    """Fetch JSON data from URLs."""

    def fetch(self, url: str) -> dict:
        # Placeholder for requests.get
        return {"url": url}
