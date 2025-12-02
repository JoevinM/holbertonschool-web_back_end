#!/usr/bin/env python3

"""
Calculate the start and end indexes for pagination based on the given page
number and page size. Page numbers start at 1, and the returned tuple
contains the range of item indexes to be returned for the requested page.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of (start_index, end_index)
    corresponding to the range of items to return
    for a given page and page size.
    """

    start = (page - 1) * page_size
    end = page * page_size
    index = (start, end)
    return index
