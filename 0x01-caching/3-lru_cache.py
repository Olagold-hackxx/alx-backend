#!/usr/bin/python3
"""LRU cache dictionary"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRU cache"""
    def __init__(self):
        """Initiate class"""
        super().__init__()
        self.recently_used = OrderedDict()

    def put(self, key, item):
        """ Store to cache"""
        if key is not None or item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Get least used key
                lru_key, _ = self.recently_used.popitem(last=False)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
            self.recently_used[key] = None
            self.cache_data[key] = item

    def get(self, key):
        """ Get from cache"""
        if key not in self.cache_data.keys() or key is None:
            return None
        self.recently_used.move_to_end(key)
        return self.cache_data[key]
