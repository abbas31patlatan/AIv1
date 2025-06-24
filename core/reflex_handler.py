"""Trigger reflex actions based on stimuli."""
from __future__ import annotations


class ReflexHandler:
    """Map stimuli to immediate actions."""

    def __init__(self) -> None:
        self.mapping: dict[str, str] = {}

    def register(self, stimulus: str, action: str) -> None:
        self.mapping[stimulus] = action

    def react(self, stimulus: str) -> str | None:
        return self.mapping.get(stimulus)
