"""Internal dialogue simulation."""
from __future__ import annotations

from nlp.response_generator import generate_response


class InternalDialogue:
    """Use the response generator to talk to itself."""

    def reflect(self, thought: str) -> str:
        return generate_response(thought)
