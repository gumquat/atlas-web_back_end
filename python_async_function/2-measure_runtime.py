#!/usr/bin/env python3

"""Description text goes here"""


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Args:
        n (int): random number
        max_delay (int, optional): max delay random number. Defaults to 10.
    Returns:
        float
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n
