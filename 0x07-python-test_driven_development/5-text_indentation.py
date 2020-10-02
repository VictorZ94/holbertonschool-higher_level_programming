#!/usr/bin/python3
"""[summary]
"""


def text_indentation(text):
    """ Doc """
    if type(text) is not str:
        raise TypeError("text must be a string")
    length = len(text)
    string = ""
    i = 0
    while i < length:
        string += text[i]
        if text[i] == ':' or text[i] == '?' or text[i] == '.':
            print("{:s}".format(string.strip()), end="")
            string = ""
            print("\n")
        i += 1
    print("{:s}".format(string.strip()))
