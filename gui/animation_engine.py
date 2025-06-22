"""Very basic animation engine."""
from __future__ import annotations

import time


def animate(frames: int, delay: float = 0.1) -> None:
    for _ in range(frames):
        time.sleep(delay)
