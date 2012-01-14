# -*- coding: utf-8 -*-
'''
Single-process in-memory LRU cache.

The shove psuedo-URL for a simple cache is:

simplelru://
'''

from shove import LRUBase

__all__ = ['SimpleLRUCache']


class SimpleLRUCache(LRUBase):

    '''In-memory cache that purges based on least recently used item.'''  