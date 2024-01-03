#!/usr/bin/env python3

"""async fun that waits random seconds"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        may_delay (int, optional): _description_. Defaults to 10.
    Returns:
        float: _description_
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
