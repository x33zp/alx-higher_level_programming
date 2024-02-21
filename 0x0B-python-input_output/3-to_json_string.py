#!/usr/bin/python3
"""
Contains a function to_json_string
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object `my_obj` into a JSON string.

    Parameters:
        my_obj (any): The Python object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the input Python object `my_obj`.

    Note:
        This function internally uses the `json.dumps()` function from the
        `json` module to perform the conversion.
    """
    return json.dumps(my_obj)
