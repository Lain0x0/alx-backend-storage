#!/usr/bin/env python3
""" Web Caching & Tracking """
import requests
import redis
from functools import wraps

x = redis.Redis()


def count_url_access(method):
    """ Couting and Tracking """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        x.incr(count_key)
        x.set(cached_key, html)
        x.expire(cached_key, 10)
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Return HTML content """
    res = requests.get(url)
    return res.text
