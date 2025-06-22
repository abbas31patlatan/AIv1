"""Default GUI preferences."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GUIPreferences:
    """Customisation options for the GUI."""

    theme: str = "light"
    voice_enabled: bool = True
    language: str = "en"


prefs = GUIPreferences()
"""Global GUI preferences."""
