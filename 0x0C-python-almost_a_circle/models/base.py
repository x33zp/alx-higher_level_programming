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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return a json representation of the parameter
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as jsonfile:
            if list_objs is None:
                jsonfile.write('[]')
            else:
                obj_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(Base.to_json_string(obj_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)
