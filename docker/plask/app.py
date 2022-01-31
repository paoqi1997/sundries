from flask import Flask

import time

import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def getHitCount():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = getHitCount()
    return 'Hello World! I have been seen {} times.\n'.format(count)
