#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary with hypermedia pagination information.

        This method retrieves a page of data starting from a given index,
        skipping
        missing entries if the dataset has been altered (deletion resilience).

        Args:
            index (int): Starting index for pagination. Must be valid.
            page_size (int): Number of items to return.

        Returns:
            Dict[str, Any]: A dictionary containing:
                - index: the starting index
                - next_index: the index to use for the next page
                - page_size: number of items actually returned
                - data: the list of returned dataset entries
        """
        assert index is not None
        assert 0 <= index < len(self.indexed_dataset())

        dataset = self.indexed_dataset()
        data = []
        current = index

        while len(data) < page_size and current < len(dataset):
            if current in dataset:
                data.append(dataset[current])
            current += 1

        next_index = current

        dictionnary = {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }

        return dictionnary
