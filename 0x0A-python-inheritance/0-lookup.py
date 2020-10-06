#!/usr/bin/python3
"""[summary]
"""


def lookup(obj):
    """Return Attribute and methods
    of a object.
    """
    mylist = []
    mylist = dir(obj)
    return mylist
