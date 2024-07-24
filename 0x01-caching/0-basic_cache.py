#!/usr/bin/env python3
"""Python Module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a caching system that inherits from BaseCaching.

    This caching system has no limit on the number of items it can store.
    """

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: the key under which the item should be stored.
            item: the item to store.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key from the cache.

        Args:
            key: the key of the item to retrieve.

        Returns:
            The value in self.cache_data linked to key.
            Return None if the key is None or doesn't exist in self.cache_data
        """
        return self.cache_data.get(key, None)
