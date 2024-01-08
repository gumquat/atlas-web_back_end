#!/usr/bin/python3

"""Description text goes here"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class"""

    def __init__(self):
        """init LRUCache"""
        super().__init__()
        self.order_used = []


    def put(self, key, item):
        """add an item ot the cache"""
        if key is not None and item is not None:  # is the key / item not None?
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:  # is cache full?
                last_key = self.order_used.pop(0)  # del most recent key from used
                del self.cache_data[last_key]  # remove the item from the cache
                print("DISCARD:", last_key)  # print the discarded key

            self.order_used.append(key)  # update the order of the used keys
            self.cache_data[key] = item  # add the item to the cache


    def get(self, key):
        """retrievce an item from the cache"""
        if key is not None or key not in self.cache_data:
            return None

        self.order_used.remove(key)  # remove the key from the used keys
        self.order_used.append(key)  # add the key to the end of the used keys
        return self.cache_data[key]  # return the item from the cache
