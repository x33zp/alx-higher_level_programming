#!/usr/bin/python3
"""
contains function class_to_json
"""


def class_to_json(obj):
    """
    Returns a dictionary representation of the object suitable for
    JSON serialization.

    Returns:
        dict: A dictionary representing the object with serializable
        attributes.

    Note:
        This function assumes that the object has a `__dict__` attribute, which
        contains
        all the attributes and their values of the object. It directly returns this
        dictionary,
        which may include non-serializable attributes.

        It's recommended to use this function only when you're sure that all attributes of
        the object are serializable (i.e., they are of types list, dictionary, string,
        integer, or boolean).
    """
    return obj.__dict__
