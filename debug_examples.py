import os
from debug import debug_func, debug_instance_methods


@debug_func
def spam():
    """example of debug_fun
    """
    return 1


@debug_instance_methods
class Spam:
    def instance_method(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass


if __name__ == "__main__":
    spam()
    Spam().instance_method()
    Spam().class_method()
    Spam().static_method()
