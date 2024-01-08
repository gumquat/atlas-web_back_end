#!/usr/bin/python3

"""A class BasicCache that inherits from BaseCaching and is a caching system"""


class BaseCaching:
    def __init__(self):
        self.cache_data = {}

class BasicCache(BaseCaching):
    """
    Args:
        BaseCaching (_type_): _description_
    """
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
