#!/usr/bin/python3
"""[summary]
"""


def print_square(size):
    """[summary]

    Args:
        size ([type]): [description]

    Raises:
        TypeError: [description]
        TypeError: [description]
        ValueError: [description]
    """
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
