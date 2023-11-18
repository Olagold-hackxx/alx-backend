#!/usr/bin/python3
"""Basic cache dictionary"""
from base_cache import BaseCaching

class BasicCache(BaseCaching):
    """ Basic cache"""
    def put(self, key, item):
        """ Store to cache"""
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get from cache"""
        if key not in self.cache_data.keys() or key is None:
            return None
        return self.cache_data[key]
