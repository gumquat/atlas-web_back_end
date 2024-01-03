#!/usr/bin/env python3

"""returns list of random wait times"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List:
    """
    Args:
        n (int): _description_
        max_delay (int, optional): _description_. Defaults to 10.
    Returns:
        List: _description_
    """
    delay_list = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delay_list)
