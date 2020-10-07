#!/usr/bin/python3
"""Function to read a file
"""


def read_file(filename=""):
    """print read file
    Args:
        filename (pathname, format or mode) Defaults to "".
    """
    with open(filename, mode="rt", encoding="UTF8") as myFile:
        print(myFile.read())
