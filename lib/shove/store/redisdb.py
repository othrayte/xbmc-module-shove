# -*- coding: utf-8 -*-
'''
Redis-based object store

The shove psuedo-URL for a redis-based store is:

redis://<host>:<port>/<db>
'''

import urlparse

try:
    import redis
except ImportError:
    raise ImportError('This store requires the redis library')

from shove.store.simple import SimpleStore

__all__ = ['RedisStore']


class RedisStore(SimpleStore):

    '''Redis based store'''

    init = 'redis://'

    def __init__(self, engine, **kw):
        super(RedisStore, self).__init__(engine, **kw)
        spliturl = urlparse.urlsplit(engine)
        host, port = spliturl[1].split(':')
        db = spliturl[2].replace('/', '')
        self._store = redis.Redis(host, int(port), db)

    def __getitem__(self, key):
        item = super(RedisStore, self).__getitem__(key)
        if item is not None: 
            return item
        raise KeyError(key)
