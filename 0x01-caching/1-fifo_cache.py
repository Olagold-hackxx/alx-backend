#!/usr/bin/python3
"""FIFO cache dictionary"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache"""
    def __init__(self):
        """Initiate class"""
        super().__init__()
        self.insertion_order = []

    def put(self, key, item):
        """ Store to cache"""
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.insertion_order[0]
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")
                self.insertion_order.pop(0)
            self.cache_data[key] = item
            self.insertion_order.append(key)

    def get(self, key):
        """ Get from cache"""
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data[key]
