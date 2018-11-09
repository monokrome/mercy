""" various generic utilities for working with objects """

import inspect


def ensure_instance(obj, *args, **kwargs):
    """ If the given object is not an instance, instantiate with given arguments """

    if inspect.isclass(obj):
        obj = obj(*args, **kwargs)

    return obj

