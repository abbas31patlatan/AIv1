"""Temporary in-memory storage."""
from __future__ import annotations


data: dict[str, str] = {}


def set_value(key: str, value: str) -> None:
    data[key] = value


def get_value(key: str) -> str | None:
    return data.get(key)
