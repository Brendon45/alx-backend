#!/usr/bin/env python3
""" Python Module """
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class implementing LRU caching mechanism"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item  # Add item to cache

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # If cache exceeds max size, remove least recently used item
            initial = self.get_first_list(self.queue)
            if initial:
                self.queue.pop(0)  # Remove from queue
                del self.cache_data[initial]  # Remove from cache
                print("DISCARD: {}".format(initial))

        if key not in self.queue:
            self.queue.append(key)  # Add new key to the end of the queue
        else:
            self.mv_last_list(key)  # Move key to the end if it already exists

    def get(self, key):
        """Retrieve an item from the cache"""
        item = self.cache_data.get(key, None)
        if item is not None:
            self.mv_last_list(key)  # Move accessed key to the end of the queue
        return item

    def mv_last_list(self, item):
        """Move an element to the end of the list"""
        length = len(self.queue)
        if self.queue[length - 1] != item:
            self.queue.remove(item)  # Remove item from its current position
            self.queue.append(item)  # Append item to the end

    @staticmethod
    def get_first_list(array):
        """Get the first element of a list"""
        return array[0] if array else None
