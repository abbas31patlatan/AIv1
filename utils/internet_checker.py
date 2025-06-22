"""Basic internet availability check."""
from __future__ import annotations

import socket


def connected(host: str = "8.8.8.8", port: int = 53, timeout: float = 0.5) -> bool:
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception:
        return False
