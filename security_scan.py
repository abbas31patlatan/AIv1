"""Perform a naive security scan."""
from __future__ import annotations


def scan(text: str) -> bool:
    return "malware" not in text.lower()
