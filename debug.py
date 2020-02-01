from functools import wraps
import os


def debug_func(func):
    """example debug decorator for function
    """
    func_name = func.__qualname__

    @wraps(func)    # wrap pull metadata from the original function such as docstring
    def wrapper(*args, **kwargs):
        # do something additional here
        # i.e: print full qualified name of the original function
        print("i am debugging " + func_name)

        return func(*args, **kwargs)  # execute the original function
    return wrapper  # return the wrapped function


def debug_instance_methods(cls):
    """decorate all instance methods (not class and static methods) with debug_func
    """
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug_func(val))
    return cls
