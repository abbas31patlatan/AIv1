"""Available GUI themes."""
from dataclasses import dataclass, field
from typing import List


@dataclass
class ThemeConfig:
    """Store theme names."""

    themes: List[str] = field(default_factory=lambda: ["light", "dark", "solar"])

    def add_theme(self, name: str) -> None:
        if name not in self.themes:
            self.themes.append(name)


themes = ThemeConfig()
