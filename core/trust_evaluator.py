"""Evaluate trust score of external input."""
from __future__ import annotations


class TrustEvaluator:
    """Return a trust value based on heuristics."""

    def rate(self, text: str) -> float:
        lowered = text.lower()
        if "error" in lowered or "warning" in lowered:
            return 0.2
        if "ok" in lowered or "success" in lowered:
            return 0.9
        return 0.5
