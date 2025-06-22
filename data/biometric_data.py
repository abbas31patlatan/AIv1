"""Store simple biometric metrics."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class BiometricData:
    """Represents user biometric readings."""

    metrics: Dict[str, float] = field(default_factory=dict)

    def record(self, name: str, value: float) -> None:
        self.metrics[name] = value
