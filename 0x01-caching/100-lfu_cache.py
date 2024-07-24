#!/usr/bin/env python3
""" Python Module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache defines a Least Frequently Used caching system
    """

    def __init__(self):
        """
        Initialize the class with the parent's init method
        """
        super().__init__()
        # List to track the order of key usage
        self.usage = []
        # Dictionary to track the frequency of key usage
        self.frequency = {}

    def put(self, key, item):
        """
        Cache a key-value pair
        """
        if key is None or item is None:
            return  # Do nothing if key or item is None

        # Check if cache has reached its max capacity
        length = len(self.cache_data)
        if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            # Find the least frequently used (LFU) keys
            lfu = min(self.frequency.values())
            lfu_keys = [k for k, v in self.frequency.items() if v == lfu]

            # If there are multiple LFU keys, discard if any
            if len(lfu_keys) > 1:
                lru_lfu = {k: self.usage.index(k) for k in lfu_keys}
                discard = min(lru_lfu.values())
                discard = self.usage[discard]
            else:
                discard = lfu_keys[0]

            # Discard the key
            print("DISCARD: {}".format(discard))
            del self.cache_data[discard]
            del self.usage[self.usage.index(discard)]
            del self.frequency[discard]

        # Update usage frequency
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        # Update usage list
        if key in self.usage:
            del self.usage[self.usage.index(key)]
        self.usage.append(key)

        # Add item to cache
        self.cache_data[key] = item

    def get(self, key):
        """
        Return the value linked to a given key, or None
        """
        if key is not None and key in self.cache_data.keys():
            # Update usage and frequency
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
