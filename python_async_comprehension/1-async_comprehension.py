#!/usr/bin/env python3

"""Description text goes here""" 

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    _summary_
    Returns:
        List[float]: 10 random numbers
    """
    results = [num async for num in async_generator()]
    return results[:10]
