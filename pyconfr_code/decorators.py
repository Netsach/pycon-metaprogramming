# -*- coding: utf-8 -*-
from functools import wraps


def decorator_base(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Wrapped !")
        return func(*args, **kwargs)

    return func


@decorator_base
def my_func(msg):
    print(msg)


my_func(msg='Hello World')
