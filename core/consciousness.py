"""Basic consciousness component."""

from __future__ import annotations

import logging
from typing import Callable, Dict, List


class Consciousness:
    """Represents a rudimentary awareness with event hooks."""

    def __init__(self) -> None:
        self._thoughts: List[str] = []
        self._hooks: Dict[str, List[Callable[..., None]]] = {}
        logging.debug("Consciousness initialised")

    def think(self, thought: str) -> None:
        """Record a *thought* and trigger hooks."""
        logging.info("Thinking: %s", thought)
        self._thoughts.append(thought)
        for func in self._hooks.get("think", []):
            func(thought)

    def on(self, event: str, func: Callable[..., None]) -> None:
        """Register *func* to execute when *event* occurs."""
        self._hooks.setdefault(event, []).append(func)
        logging.debug("Hook registered for event %s", event)

    def history(self) -> List[str]:
        """Return a copy of all recorded thoughts."""
        return list(self._thoughts)
