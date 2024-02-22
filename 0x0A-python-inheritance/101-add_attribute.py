#!/usr/bin/python3
"""
Contains function add_attribute
"""


def add_attribute(obj, att, value):
    """
    Adds a new attribute to an object if it's possible.

    Parameters:
        obj: Any - The object to which the attribute will be added.
        attr: str - The name of the attribute to be added.
        value: Any - The value of the attribute to be added.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, att, value)
    raise TypeError("can't add new attribute")
