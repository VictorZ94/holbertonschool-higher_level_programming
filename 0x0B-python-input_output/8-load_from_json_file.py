#!/usr/bin/python3
"""Doc
"""
import json


def load_from_json_file(filename):
    """
    Args:
        filename ([type]): [description]
    """
    with open(filename, "r") as myFile:
        return json.load(myFile)
