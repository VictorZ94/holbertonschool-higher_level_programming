#!/usr/bin/python3
"""[summary]
"""


def say_my_name(first_name, last_name=""):
    """[summary]

    Args:
        first_name ([type]): [description]
        last_name (str, optional): [description]. Defaults to "".

    Raises:
        TypeError: [description]
        TypeError: [description]
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
