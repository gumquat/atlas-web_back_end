#!/usr/bin/env python3

"""Description text goes here"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    Args:
        n (int): random number
        max_delay (int, optional): Defaults to 10.
    Returns:
        List[float]: returned output
    """
    delay_list = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delay_list)
