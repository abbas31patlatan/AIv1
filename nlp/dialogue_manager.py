"""Small dialogue manager coordinating NLP and memory."""

from __future__ import annotations

from memory_ import Memory

from core import consciousness
from models.gguf_loader import GGUFModel
from .response_generator import generate_response


class DialogueManager:
    """Coordinate interactions and generate simple responses."""

    def __init__(self, memory: Memory, model: GGUFModel | None = None) -> None:
        self.memory = memory
        self.model = model

    def handle_input(self, text: str) -> str:
        """Store input, log it to consciousness and generate a response."""

        consciousness.think(text)
        self.memory.add(text)
        return generate_response(text, model=self.model)
