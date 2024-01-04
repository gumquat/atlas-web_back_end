#!/usr/bin/env python3

"""Description text goes here"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Returns:
        float: returns runtimes
    """
    start = asyncio.get_event_loop().time()
    four_tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*four_tasks)
    end = asyncio.get_event_loop().time()
    result = end - start
    return result
