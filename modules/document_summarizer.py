"""Summarise short documents."""
from __future__ import annotations


def summarise(text: str, length: int = 20) -> str:
    return text[:length] + ("..." if len(text) > length else "")
