#!/usr/bin/python3
"""
This script defines the Base class, which serves as the base
for other classes in the project.
"""

import json


class Base:
    """
    Base class to manage id attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Parameters:
            - id (int): Optional. The id to assign to the instance.
            If None, a new id is generated.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        
        """
        if not len(list_dictionaries) or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
