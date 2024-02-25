#!/usr/bin/pytihon3
"""
This script defines the Base class, which serves as the base
for other classes in the project.
"""

import json
import os


class Base:
    """
    Base class to manage id attribute in all future classes.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Parameters:
            id: Optional. The id to assign to the instance.
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
        Convert a list of dictionaries to a JSON string.

        Parameters:
           list_dictionaries (list): A list of dictionaries.

        Returns:
           str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries == [] or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
         Write the JSON string representation of list_objs to
         a file.

        Parameters:
            list_objs (list): A list of instances that inherit
            from Base.

        Returns:
            Empty list if list_objs is None
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
        Convert a JSON string to a list of dictionaries.

        Parameters:
            json_string (str): A string representing a list of
            dictionaries in JSON format.

        Returns:
            list: List of dictionaries represented by json_string.
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set based on the provided
        dictionary.

        Parameters:
          **dictionary (dict): A dictionary containing attribute names
          and values.

        Returns:
            instance: An instance of the class with attributes set based
            on the dictionary.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from a JSON file and return a list of instances.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = cls.__name__ + '.json'
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                dict_list = cls.from_json_string(file.read())
                return [cls.create(**dictionary) for dictionary in dict_list]
        return []
