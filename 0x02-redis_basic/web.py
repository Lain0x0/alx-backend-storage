#!/usr/bin/env python3
""" Using redis in python for web cahing and tracking """
import requests
import redis

x = redis.Redis()


def get_page(url: str) -> str:
    """ GET method for html content """
    x.incr(f"count:{url}")

    cached = x.get(url)
    if cached:
        return cached.decode('utf-8')

    html_content = requests.get(url).text

    x.setex(url, 10, html_content)

    return html_content
