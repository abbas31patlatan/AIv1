"""Imitate detected emotion in text."""
from __future__ import annotations

from nlp.language_emotion import analyze_sentiment


def imitate(text: str) -> str:
    sentiment = analyze_sentiment(text)
    return f"*{sentiment} voice* {text}"
