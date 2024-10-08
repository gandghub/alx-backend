#!/usr/bin/env python3
"""
Basic dictionary that inherits from a base
caching module
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    def put(self, key, item):
        """adds item to a dict"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """returns a value linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
