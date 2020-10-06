#!/usr/bin/python3
"""Doc
"""


def is_kind_of_class(obj, a_class):
    """Doc"""
    value = isinstance(obj, a_class)
    if value:
        return True
    else:
        return False
