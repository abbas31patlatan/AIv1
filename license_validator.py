"""Validate license keys."""
from __future__ import annotations


def validate(key: str) -> bool:
    return key.startswith("LIC-")
