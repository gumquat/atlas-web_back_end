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


def call_history(method: Callable) -> Callable:
    """DECORATER - stores the input/output history of calls for a method
    """
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        result = method(self, *args, **kwargs)

        self._redis.rpush(input_key, str(args))
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper


class Cache:
    """CLASS - 'Cache' that implements a cache using Redis
    """
    def __init__(self):
        self._redis = redis.Redis()  # store inst. of the Redis in private var
        self._redis.flushdb()  # flush the Redis database

    @call_history
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


def replay(method: Callable) -> None:
    """gets and prints the history of calls of a specified method
    """
    methodName = method.__qualname__  # get the name of the method
    countKey = methodName  # get the number of calls of a key
    inputKey = f"{methodName}:inputs"  # get the inputs of a key
    outputKey = f"{methodName}:outputs"  # get the outputs of a key

    count = method.__self__._redis.get(countKey)  # set the number of calls
    inputs = method.__self__._redis.lrange(inputKey, 0, -1)  # set inputs
    outputs = method.__self__._redis.lrange(outputKey, 0, -1)  # set outputs

    print(f"{methodName} was called {int(count)} times:")  # make a print func
    # for each input/outputr string in the 'zip'...
    # ...print it out in the required format
    for input_str, output_str in zip(inputs, outputs):
        print(f"{methodName}(*{input_str.decode('utf-8')}) ->\
              {output_str.decode('utf-8')}")
