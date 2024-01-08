#!/usr/bin/python3

"""Description text goes here"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching"""
    def __init__(self):
        """inits FIFOCache"""
        super().__init__()
        self.cache_keys = []

    def put(self, key, item):
        """
        adds an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.cache_keys:
                self.cache_keys.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = self.cache_keys.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

    def get(self, key):
        """
        retrieves an item from the cache
        """
        return self.cache_data.get(key, None)
