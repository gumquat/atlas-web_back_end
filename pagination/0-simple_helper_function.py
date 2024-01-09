#!/usr/bin/env python3

"""Description text goes here"""


def index_range(page, page_size):
    """
    Args:
        page (_type_): number of current page
        page_size (_type_): total number of pages
    Returns:
        _type_: tuple of start and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
