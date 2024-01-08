#!/usr/bin/python3

"""Description text goes here"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""

    def __init__(self):
        """init MRUCache"""
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """adds item to console"""
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = max(self.cache_data, key=self.cache_data.get)
                del self.cache_data[last_key]
                print("DISCARD:", last_key)

            self.cache_data[key] = item

    def get(self, key):
        """retrieve item from cache"""
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)  # Remove the key from the cache
        self.cache_data[key] = value  # Add the key to the end of the cache

        return value
