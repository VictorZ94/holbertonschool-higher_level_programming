#!/usr/bin/python3
"""To change JSON to string
"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj ([type]): [description]
    Returns:
        object: return data type
    """
    string = json.dumps(my_obj)
    return string
