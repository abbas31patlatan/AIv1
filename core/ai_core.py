"""Minimal orchestrator tying memory and dialogue together."""
from __future__ import annotations

from memory_ import Memory
from nlp.dialogue_manager import DialogueManager
from models.gguf_loader import GGUFModel


class AICore:
    """Coordinate memory storage and dialogue response."""

    def __init__(self, model: GGUFModel | None = None) -> None:
        self.memory = Memory()
        self.dialogue = DialogueManager(self.memory, model=model)

    def interact(self, text: str) -> str:
        """Process *text* and return a reply."""
        return self.dialogue.handle_input(text)
