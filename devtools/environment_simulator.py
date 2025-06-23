"""Simulate certain environment variables."""
from __future__ import annotations

import os


def set_env(key: str, value: str) -> None:
    os.environ[key] = value
