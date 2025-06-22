"""Wrapper around :mod:`cProfile` for quick profiling."""
from __future__ import annotations

import cProfile
import pstats
from io import StringIO


def profile(func, *args, **kwargs) -> str:
    profiler = cProfile.Profile()
    profiler.enable()
    func(*args, **kwargs)
    profiler.disable()
    buf = StringIO()
    stats = pstats.Stats(profiler, stream=buf)
    stats.sort_stats(pstats.SortKey.CUMULATIVE)
    stats.print_stats()
    return buf.getvalue()
