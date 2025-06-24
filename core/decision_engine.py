"""Basic rule based decision engine."""
from __future__ import annotations


class DecisionEngine:
    """Evaluate simple conditions to choose an action."""

    def choose(self, sentiment: str) -> str:
        if sentiment == "positive":
            return "encourage"
        if sentiment == "negative":
            return "support"
        return "neutral"
