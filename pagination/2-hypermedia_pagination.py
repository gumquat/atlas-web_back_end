#!/usr/bin/env python3

"""Description text goes here"""
import csv
import math
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
            page (int, optional): Defaults to 1.
            page_size (int, optional): Defaults to 10.
        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0,\
            "Page size must be an integer greater than 0."

        start_index, end_index = index_range(page, page_size)

        with open('Popular_Baby_Names.csv', 'r', newline='', encoding='utf-8')\
                as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)

            return rows[start_index:end_index] if start_index < len(rows) \
                else []


def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    """
    Args:
        page (int, optional): Defaults to 1.
        page_size (int, optional): Defaults to 10.
    Returns:
        dict: dictionary containing page details
    """
    assert isinstance(page, int) and page > 0, \
        "Page must be an integer greater than 0."
    assert isinstance(page_size, int) and page_size > 0,\
        "Page size must be an integer greater than 0."

    dataset = self.dataset()
    total_records = len(dataset)
    total_pages = math.ceil(total_records / page_size)

    start_index, end_index = index_range(page, page_size)

    with open('Popular_Baby_Names.csv', 'r', newline='', encoding='utf-8')\
            as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

        data = rows[start_index:end_index] if start_index < len(rows) \
            else []

    hyper_info = {
        'page_size': len(data),
        'page': page,
        'data': data,
        'next_page': page + 1 if page < total_pages else None,
        'prev_page': page - 1 if page > 1 else None,
        'total_pages': total_pages
    }

    return hyper_info
