#!/usr/bin/env python3
"""
Pagination
"""


def index_range(page: int, page_size: int) -> tuple:
    """ Get index"""
    start_index = (page_size * page) - page_size
    end_index = page_size * page
    return start_index, end_index
