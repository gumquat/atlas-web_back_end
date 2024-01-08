#!/usr/bin/python3

"""Description text goes here"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class
    """
    def __init__(self):
        """
        init LIFOCache
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        add item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieve an item from the cache
        """
        return self.cache_data.get(key, None)
