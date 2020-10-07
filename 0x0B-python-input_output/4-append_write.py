#!/usr/bin/python3
"""Doc
"""


def append_write(filename="", text=""):
    """Doc
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
        length = len(text)
        return length
