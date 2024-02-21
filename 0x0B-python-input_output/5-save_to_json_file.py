#!/usr/bin/python3
"""
Contains function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object `my_obj` to a text file using a JSON representation.

    Parameters:
        my_obj (any): The Python object to be serialized and saved to the file.
        filename (str): The name of the file to which the JSON representation
        will be saved.

    Note:
        This function uses the `json.dump()` function from the `json` module to
        serialize the input Python object `my_obj` into a JSON string and save
        it to the specified file.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
