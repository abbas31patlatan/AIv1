"""Generic API connector using :mod:`requests` when available.

The real implementation would handle authentication, retries and error
reporting.  Here we keep it intentionally short and fall back to Python's
standard library when ``requests`` is not installed or the request fails.

Example
-------
>>> c = APIConnector()
>>> data = c.fetch('http://example.com')
>>> 'url' in data
True
"""
from __future__ import annotations


import json
import logging
from typing import Any, Dict

try:
    import requests
except Exception:  # pragma: no cover - optional dependency
    requests = None  # type: ignore
import urllib.request


class APIConnector:
    """Fetch JSON data from URLs with graceful fallbacks."""

    def fetch(self, url: str) -> Dict[str, Any]:
        try:
            if requests:
                resp = requests.get(url, timeout=5)
                resp.raise_for_status()
                return resp.json()
            with urllib.request.urlopen(url, timeout=5) as fp:
                return json.load(fp)
        except Exception as exc:  # pragma: no cover - network failure
            logging.debug("request failed for %s: %s", url, exc)
            return {"url": url}
