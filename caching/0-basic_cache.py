#!/usr/bin/python3

"""A class BasicCache that inherits from BaseCaching and is a caching system"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    We cashing basics :sunglasses:
    """

    def put(self, key, item):
        """
        adds an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieves an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
