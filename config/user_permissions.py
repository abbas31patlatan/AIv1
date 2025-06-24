"""User permission configuration."""
from dataclasses import dataclass, field
from typing import Set


@dataclass
class UserPermissions:
    """Maintain a whitelist of allowed operations."""

    allowed: Set[str] = field(default_factory=set)

    def grant(self, permission: str) -> None:
        self.allowed.add(permission)

    def revoke(self, permission: str) -> None:
        self.allowed.discard(permission)


permissions = UserPermissions()
