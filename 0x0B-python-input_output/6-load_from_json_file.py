#!/usr/bin/python3
"""
Contains function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Parameters:
        filename (str): The name of the JSON file from which the object will be
        created.

    Returns:
        any: The Python object created from the JSON data.

    Note:
        This function uses the `json.load()` function from the `json` module
        to deserialize the JSON data from the specified file into a Python
        object.
    """
    with open(filename, 'r') as file:
        return json.load(file)
