"""Tiny load test utility."""
from __future__ import annotations

import time


def run(repeat: int, func) -> float:
    start = time.time()
    for _ in range(repeat):
        func()
    return time.time() - start
