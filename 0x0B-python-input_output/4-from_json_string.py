#!/usr/bin/python3
"""
Contains function from_json_string
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON string `my_str` into a Python object.

    Parameters:
        my_str (str): The JSON string to be converted into a Python object.

    Returns:
        The Python object representation of the input JSON string `my_str`.

    Note:
        This function internally uses the `json.loads()` function from the
        `json` module to perform the conversion.
    """
    return json.loads(my_str)
