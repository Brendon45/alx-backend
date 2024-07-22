#!/usr/bin/env python3
"""A function - idx_range that takes two integer argumnts page & page_size"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing a start"""
    start = (page - 1) * page_size
    end = page * page_size

    return start, end
