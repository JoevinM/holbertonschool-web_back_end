#!/usr/bin/env python3
"""
Return a dictionary containing hypermedia pagination information for
the requested page. The method validates input values, retrieves the
appropriate page of the dataset using get_page, and computes useful
metadata such as total pages, next page, and previous page to support
hypermedia-driven pagination.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:

        """
        Return a page of the dataset based on
        the given page number and page size.
        This method validates the inputs, computes the pagination range using
        index_range, and returns the corresponding slice of the cached dataset.
        """

        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0
        data = self.dataset()
        start, end = index_range(page, page_size)
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:

        """
        Return a dictionary containing hypermedia pagination metadata for the
        requested page. This includes the current page number, the actual page
        size, the dataset slice, and information allowing navigation between
        pages such as next and previous page numbers.
        """

        assert isinstance(page, int)
        assert page > 0
        assert isinstance(page_size, int)
        assert page_size > 0

        data = self.get_page(page, page_size)
        total_pages = (math.ceil(len(self.dataset()) / page_size))

        if page > 1:
            prev_page = page - 1
        else:
            prev_page = None
        if page < total_pages:
            next_page = page + 1
        else:
            next_page = None

        dictionnary = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return dictionnary


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple of (start_index, end_index)
    corresponding to the range of items to return
    for a given page and page size.
    """

    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
