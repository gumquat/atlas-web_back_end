#!/usr/bin/env python3

"""Description text goes here"""
import asyncio
import random


async def async_generator():
    """
    _summary_
    loops 10 times
    waits a second in async
    returns random # from 1-10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
