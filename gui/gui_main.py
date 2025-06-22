"""Entry point for the text-based GUI."""
from __future__ import annotations

from .gui_elements import button


def run() -> str:
    return button("Start")
