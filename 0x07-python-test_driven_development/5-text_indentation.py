#!/usr/bin/python3
"""[summary]
"""


def text_indentation(text):
    """[summary]

    Args:
        text ([type]): [description]

    Raises:
        TypeError: [description]
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    for i in range(len(text)):
        if text[i] == ' ' and text[i-1] == '?' or text[i-1] \
                == '.' or text[i-1] == ':':
            None
        else:
            print("{}".format(text[i]), end="")
        if text[i] == ':' or text[i] == '?' or text[i] == '.':
            print("\n")
        i += 1
    print("")
