#!/usr/bin/env python3
import csv
import math
from typing import List
"""
Simple Pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """ Get index"""
    start_index = (page_size * page) - page_size
    end_index = page_size * page
    return start_index, end_index


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
        """Simple pagination"""
        assert (type(page) == int and page > 0)
        assert (type(page_size) == int and page_size > 0)
        index = index_range(page, page_size)
        dataset = self.dataset()
        return dataset[index[0]: index[1]]
