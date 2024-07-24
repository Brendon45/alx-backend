#!/usr/bin/env python3
""" Python Module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class implementing MRU caching mechanism"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        # List to keep track of access order
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return  # Do nothing if key or item is None

        self.cache_data[key] = item  # Add item to cache

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # If cache exceeds max size, remove most recently used item
            if self.queue:
                # Remove last accessed item from queue
                last = self.queue.pop()
                # Remove it from cache
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

        if key not in self.queue:
            # Add new key to the end of the queue
            self.queue.append(key)
        else:
            # Move key to the end if it already exists
            self.mv_last_list(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        item = self.cache_data.get(key, None)
        if item is not None:
            # Move accessed key to the end of the queue
            self.mv_last_list(key)
        return item

    def mv_last_list(self, item):
        """Move an element to the end of the list"""
        length = len(self.queue)
        if self.queue[length - 1] != item:
            # Move accessed key to the end of the queue
            self.queue.remove(item)
            # Append item to the end
            self.queue.append(item)
