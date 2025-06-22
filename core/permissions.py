"""Permission checking utilities."""
from __future__ import annotations

from config.user_permissions import permissions


def has_permission(name: str) -> bool:
    """Return ``True`` if *name* permission is granted."""
    return name in permissions.allowed
