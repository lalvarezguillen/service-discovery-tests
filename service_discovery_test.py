import logging
import os
import time

import redis

DUMMY_KEY = 'dummy-key'
REDIS_HOST = os.environ.get("REDIS_HOST")
REDIS_PORT = os.environ.get("REDIS_PORT")

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.DEBUG)

def increment_and_log(conn: redis.Redis):
    while True:
        conn.incr(DUMMY_KEY)
        LOGGER.warning(conn.get(DUMMY_KEY))
        time.sleep(5)


if __name__ == '__main__':
    client = redis.Redis(
        host=REDIS_HOST,
        port=REDIS_PORT
    )
    client.set(DUMMY_KEY, 0)
    increment_and_log(client)
