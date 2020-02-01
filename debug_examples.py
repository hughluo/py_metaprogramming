import os
from debug import debug_func


@debug_func
def spam():
    """example of debug_fun
    """
    return 1


if __name__ == "__main__":
    spam()
