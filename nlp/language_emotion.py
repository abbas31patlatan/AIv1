"""Naive sentiment analysis based on word lists."""

from __future__ import annotations

from typing import Literal

_POSITIVE = {"great", "good", "awesome", "nice", "happy"}
_NEGATIVE = {"bad", "terrible", "awful", "sad", "angry"}

Sentiment = Literal["positive", "negative", "neutral"]


def analyze_sentiment(text: str) -> Sentiment:
    """Return an extremely naive sentiment label for *text*."""
    words = set(text.lower().split())
    pos = len(words & _POSITIVE)
    neg = len(words & _NEGATIVE)
    if pos > neg:
        return "positive"
    if neg > pos:
        return "negative"
    return "neutral"
