"""Manage high-level AI goals."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class AIGoals:
    """Container storing desired goals for the agent."""

    goals: List[str] = field(default_factory=lambda: ["learn", "assist"])

    def add_goal(self, goal: str) -> None:
        self.goals.append(goal)

    def remove_goal(self, goal: str) -> None:
        if goal in self.goals:
            self.goals.remove(goal)


goals = AIGoals()
"""Default goals used system-wide."""
