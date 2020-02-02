from inspect import Parameter, Signature


def make_signature(names):
    """return signature from list of parameter names
    """
    parameters = (Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
                  for name in names)
    signature = Signature(parameters)
    return signature


def add_signature(*names):
    """class decorator that set __signature__ attribute
    """
    def wrapper(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return wrapper


class Structure:
    """Base class that bind signature to init method
    """

    def __init__(self, *args, **kwargs):
        bound = self.__class__.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)
