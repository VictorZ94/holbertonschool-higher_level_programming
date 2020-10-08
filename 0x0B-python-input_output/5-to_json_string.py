#!/usr/bin/python3
"""To change JSON to string
"""


def to_json_string(my_obj):
    import json
    """
    Args:
        my_obj ([type]): [description]
    Returns:
        object: return data type
    """
    string = json.dumps(my_obj)
    return string
