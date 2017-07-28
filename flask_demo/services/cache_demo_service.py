import time
from flask_demo.extensions import cache


@cache.cached(timeout=86400, key_prefix='cache_demo')
def cache_demo():
    time.sleep(10)
    return 1
