"""Tiny productivity helper."""
from __future__ import annotations


def todo_summary(tasks: list[str]) -> str:
    return f"{len(tasks)} tasks pending"
