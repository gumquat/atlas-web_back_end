#!/usr/bin/env python3
"""MODULE - defines the Cache class using Redis
"""
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """DECORATER - counts for a key the number of times a method is called
    """
    resultKey = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(resultKey)
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """CLASS - 'Cache' that implements a cache using Redis
    """
    def __init__(self):
        self._redis = redis.Redis()  # store inst. of the Redis in private var
        self._redis.flushdb()  # flush the Redis database

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """METHOD - gen random key and store data in Redis
        Returns:
            str: the random key
        """
        resultKey = str(uuid.uuid4())
        self._redis.set(resultKey, data)
        return resultKey

    def get(self, key: str, fn: Optional[Callable] = None) -> \
        Union[str, bytes, int, float]:
        """METHOD - get all data from Redis using a given key
        """
        result = self._redis.get(key)  # get/store some data from Redis

        if result is not None and fn:  # if result !None and fn is defined
            result = fn(result)  # apply the passed function 'fn' to result
        return result

    def get_str(self, key: str) -> Optional[str]:
        """METHOD - get type 'str' data from Redis using a given key
        """
        result = self.get(key, str)
        return result

    def get_int(self, key: str) -> Optional[int]:
        """METHOD - get type 'int' data from Redis using a given key
        """
        result = self.get(key, int)
        return result
