"""Dummy vision detection."""
from __future__ import annotations


def detect(img: str) -> list[str]:
    return ["object"] if img else []
