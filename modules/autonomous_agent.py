"""Minimal autonomous agent that decides next action."""
from __future__ import annotations

from core.decision_engine import DecisionEngine
from nlp.language_emotion import analyze_sentiment


class AutonomousAgent:
    """Analyse text and choose an action."""

    def __init__(self) -> None:
        self.engine = DecisionEngine()

    def act(self, text: str) -> str:
        sentiment = analyze_sentiment(text)
        return self.engine.choose(sentiment)
