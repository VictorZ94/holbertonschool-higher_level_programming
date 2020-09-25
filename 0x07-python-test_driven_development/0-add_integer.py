#!/usr/bin/python3
""" add two number module
 Args:
        a (int, float): [number argument to cast to int whether is float]
        b (int, float): [to cast to int whether is float]. Defaults to 98.
"""


def add_integer(a, b=98):
    """[add integers]

    Raises:
        TypeError: [a must be an integer]
        TypeError: [b must be an integer]

    Returns:
        [add]: [function that adds 2 integers.]
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return a + b
