#!/usr/bin/env python3
import redis
import uuid
from typing import Union, Callable
from functools import wraps
""" Importing necessary libraries """


def count_calls(method: Callable) -> Callable:
    """ Returning callable function """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Using warpper """
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Storing the history of inputs and outputs in function """
    @wraps(method)
    def wrapper(self, *args):
        """ wrapper """
        input = str(args)
        self._redis.rpush(f"{method.__qualname__}:inputs", input)

        output = method(self, *args)
        self._redis.rpush(f"{method.__qualname__}:outputs", output)

        return output
    return wrapper


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
