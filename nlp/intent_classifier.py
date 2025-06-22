"""Very small keyword based intent classifier."""

from __future__ import annotations

from typing import Literal

Intent = Literal["greet", "bye", "unknown"]


def classify_intent(text: str) -> Intent:
    """Classify *text* into a very small set of intents."""
    tokens = text.lower().split()
    if any(token in ("hi", "hello", "hey") for token in tokens):
        return "greet"
    if any(token in ("bye", "goodbye") for token in tokens):
        return "bye"
    return "unknown"
