#!/usr/bin/python3
"""Doc
"""


def inherits_from(obj, a_class):
    """Doc"""
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
