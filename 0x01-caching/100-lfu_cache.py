from base_caching import BaseCaching
from collections import defaultdict

class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = defaultdict(int)
        self.recently_used = {}

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_key = [k for k, v in self.frequency.items() if v == min_freq]
            if len(lfu_key) > 1:
                lru_key = min(lfu_key, key=lambda k: self.recently_used.get(k, 0))
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.recently_used[lru_key]
                print(f"DISCARD: {lru_key}")
            else:
                lfu_key = min(lfu_key, key=lambda k: self.frequency[k])
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                del self.recently_used[lfu_key]
                print(f"DISCARD: {lfu_key}")
        self.cache_data[key] = item
        self.recently_used[key] = len(self.recently_used) + 1
        self.frequency[key] += 1

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        self.recently_used[key] = len(self.recently_used) + 1
        self.frequency[key] += 1
        return self.cache_data[key]
