#!/usr/bin/python3
"""JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj ([type]): [description]
        filename ([type]): [description]
    """
    with open(filename, "w") as myFile:
        json.dump(my_obj, myFile)
