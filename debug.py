from functools import wraps
import os


def debug_func(func):

    func_name = func.__qualname__

    @wraps(func)    # wrap pull metadata from the original function such as docstring
    def wrapper(*args, **kwargs):
        # do something additional here
        # i.e: print full qualified name of the original function
        print("i am debugging " + func_name)

        return func(*args, **kwargs)  # execute the original function
    return wrapper  # return the wrapped function
