"""
redis-py - The Python interface to the Redis key-value store.
https://github.com/andymccurdy/redis-py
"""

import redis

REDIS_URL = "redis://192.168.1.1:6379/"

    
if __name__ == '__main__':
    r = redis.Redis.from_url(url=REDIS_URL)
    p = r.pubsub()
    p.subscribe('my-first-channel')
    
    r.publish('my-first-channel', 'some data')
    
    try:
        for message in p.listen():
            print(message)  # {'channel': 'my-first-channel', 'data': 'some data', 'pattern': None, 'type': 'message'}
            # do something with the message
            
    except (KeyboardInterrupt, Exception):
        p.close()
