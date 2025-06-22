"""System metrics collector."""
from __future__ import annotations

import os


def cpu_count() -> int:
    return os.cpu_count() or 1
