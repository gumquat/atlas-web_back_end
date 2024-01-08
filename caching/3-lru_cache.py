#!/usr/bin/env python3

""" 3-lru_cache """
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class """

    def __init__(self):
        """ Initialize LRUCache instance """
        super().__init__()
        self.order_used = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the least recently used key and remove it from the cache
                discarded_key = self.order_used.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

            # Update the order_used list with the most recently used key
            self.order_used.append(key)
            # Add the item to the cache
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is None or key not in self.cache_data:
            return None

        # Update the order_used list with the most recently used key
        self.order_used.remove(key)
        self.order_used.append(key)

        return self.cache_data[key]
