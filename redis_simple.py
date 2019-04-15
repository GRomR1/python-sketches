"""
redis-py - The Python interface to the Redis key-value store.

https://github.com/andymccurdy/redis-py
"""

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

r.set('foo', 'bar')  # True
r.get('foo')  # 'bar'
