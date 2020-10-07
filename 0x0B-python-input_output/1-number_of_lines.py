#!/usr/bin/python3
"""Function to count number of lines
"""


def number_of_lines(filename=""):
    """
    Args:
        filename (pathname, format:utf-8): Defaults to "".
    Returns:
        type:int: numbers of line read
    """
    with open(filename, encoding="utf-8") as myFile:
        lines = 0
        while myFile.readline():
            lines += 1
        return lines
