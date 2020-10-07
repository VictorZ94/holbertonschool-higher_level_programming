#!/usr/bin/python3
"""Function to print lines given
"""


def read_lines(filename="", nb_lines=0):
    """
    Args:
        filename (str, pathname): [path of file]. Defaults to "".
        nb_lines (int, numberlines): [indicate numbers lines to print].
    """
    with open(filename, encoding="UTF-8") as myFile:
        check = 0
        while True:
            line = myFile.readline()
            if not line:
                break
            if check < nb_lines or nb_lines <= 0:
                print(line[:-1])
            check += 1
