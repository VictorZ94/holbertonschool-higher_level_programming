#!/usr/bin/python3
"""Function to write content into a file
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str, pathname): [path of file]. Defaults to "".
        text (str, text): text to write into file. Defaults to "".
    Returns:
        int: length of the content file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        length = len(text)
        return length
