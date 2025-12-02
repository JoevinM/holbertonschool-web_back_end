#!/usr/bin/env python3


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of (start_index, end_index)
    corresponding to the range of items to return
    for a given page and page size.
    """

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
