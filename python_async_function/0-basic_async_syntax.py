#!/usr/bin/env python3

"""asynchronous functon that waits a random number of seconds"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
    max_delay (int, optional): Defaults to 10.
    Returns: random wait time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
