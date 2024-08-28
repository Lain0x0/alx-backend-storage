#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable
from functools import wraps
from unittest.mock import call
""" Importing necessary libraries """


class Cache:
    def __init__(self):
        """ Initialize & Set up redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Initialize store prototype """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return (key)
