#!/usr/bin/python3
"""
contains the function is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object belongs to the specified class.

    Parameters:
        obj: Any - The object to be checked.
        a_class: class - The class to compare against.

    Returns:
        bool: True if the object belongs to the specified class,
              False otherwise.
    """
    return type(obj) is a_class
