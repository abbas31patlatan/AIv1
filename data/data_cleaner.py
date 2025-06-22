"""Simple text cleaner utility."""
from __future__ import annotations

import re


_CLEAN_RE = re.compile(r"[^a-zA-Z0-9 ]+")


def clean(text: str) -> str:
    """Return lowercase alphanumeric text."""
    return _CLEAN_RE.sub("", text).lower()
