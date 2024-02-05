#!/usr/bin/env python3
"""MODULE - defines the Cache class using Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

class Cache:
    """CLASS - 'Cache' that implements a cache using Redis
    """
    def __init__(self):
        self._redis = redis.Redis()  # store inst. of the Redis in private var
        self._redis.flushdb()  # flush the Redis database

    def store(self, data: Union[int, str, bytes, float]) -> str:
        """METHOD - gen random key and store data in Redis
        Args:
            key (str): 
            value (str):
        Returns:
            str: the random key
        """
        resultKey = str(uuid.uuid4())
        self._redis.set(resultKey, data)
        return resultKey
