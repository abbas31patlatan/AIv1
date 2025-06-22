"""Debug helper providing a `set_trace` like function."""
from __future__ import annotations

import pdb


def debug() -> None:
    pdb.set_trace()
