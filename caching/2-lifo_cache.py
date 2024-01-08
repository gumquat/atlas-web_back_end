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
            self.cache_data[key] = item
            if key not in self.key_order:
                self.key_order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.key_order.pop(-1)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """
        retrieve an item from the cache
        """
        return self.cache_data.get(key, None)
