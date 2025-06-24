"""Responsive layout utilities."""
from __future__ import annotations


def layout(window_width: int) -> str:
    return "mobile" if window_width < 600 else "desktop"
