#!/usr/bin/env python3

"""Description text goes here"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """
    Args:
        max_delay (int):
    Returns:
        asyncio.Task:
    """
    return asyncio.create_task(wait_random(max_delay))
