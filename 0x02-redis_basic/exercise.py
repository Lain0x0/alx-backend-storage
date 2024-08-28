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

    def get(self, key: str,
            fn: callable = None) -> Union[str, bytes, int, float]:
        """ redis data manipulation GET method """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ redis cache GET methos as string """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ redis cache GET method as integer """
        return self.get(key, int)
