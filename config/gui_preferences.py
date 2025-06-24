"""Default GUI preferences.

This module exposes a small :class:`GUIPreferences` dataclass used by the GUI
layer to persist user customisation.  Preferences can be toggled at runtime and
are saved to ``gui_prefs.json`` under ``settings.data_path``.  The helper
functions keep the example lightweight while demonstrating how simple runtime
configuration might be stored.

Example
-------
>>> from config.gui_preferences import prefs
>>> prefs.toggle_voice()
>>> prefs.set_theme("dark")
>>> prefs.save()
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path

from config.settings import settings
from utils.json_handler import load_json, save_json

@dataclass
class GUIPreferences:
    """Customisation options for the GUI."""

    theme: str = "light"
    voice_enabled: bool = True
    language: str = "en"

    def toggle_voice(self) -> None:
        """Invert the :attr:`voice_enabled` flag."""
        self.voice_enabled = not self.voice_enabled

    def set_theme(self, theme: str) -> None:
        """Update the active *theme* name."""
        self.theme = theme

    # persistence -----------------------------------------------------
    def save(self) -> None:
        """Persist current preferences to ``gui_prefs.json``."""
        path = Path(settings.data_path) / "gui_prefs.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        save_json(path, asdict(self))

    def load(self) -> None:
        """Load preferences from disk if available."""
        path = Path(settings.data_path) / "gui_prefs.json"
        if path.exists():
            data = load_json(path)
            self.theme = data.get("theme", self.theme)
            self.voice_enabled = data.get("voice_enabled", self.voice_enabled)
            self.language = data.get("language", self.language)


prefs = GUIPreferences()
"""Global GUI preferences."""

# Load stored preferences on import so the GUI reflects the last used values
prefs.load()
