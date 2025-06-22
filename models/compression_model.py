"""Simple compression ratio estimator."""
from __future__ import annotations


def ratio(original_size: int, compressed_size: int) -> float:
    return compressed_size / original_size if original_size else 0.0
