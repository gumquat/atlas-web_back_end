#!/usr/bin/env python3

"""returns a list of randomly generated wait times"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List:
    """
    Args:
        n (int): random number
        max_delay (int, optional): Defaults to 10.
    Returns:
        List: list of randomly generated wait times
    """
    delay_list = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delay_list)
