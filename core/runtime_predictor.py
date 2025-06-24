"""Estimate runtime of operations."""
from __future__ import annotations

import time


class RuntimePredictor:
    """Very naive runtime estimation using averages."""

    def __init__(self) -> None:
        self.samples: list[float] = []

    def sample(self, duration: float) -> None:
        self.samples.append(duration)

    def estimate(self) -> float:
        return sum(self.samples) / len(self.samples) if self.samples else 0.0
