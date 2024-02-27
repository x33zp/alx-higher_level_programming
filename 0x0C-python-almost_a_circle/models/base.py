#!/usr/bin/python3
"""
This script defines the Base class, which serves as the base
for other classes in the project.
"""

import json
import os
import csv
import turtle


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
            return "[]"
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serialize a list of objects into CSV format and write to a file.

        Parameters:
            list_objs (list): A list of instances that inherit
                from Base.

        Returns:
            None
        """
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline='') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            writer = csv.writer(csvfile)
            for obj in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow([obj.id, obj.width, obj.height, obj.x,
                                    obj.y])
                elif cls.__name__ == 'Square':
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialize objects from a CSV file and return a list of instances.

        Returns:
            list: List of instances loaded from the file.
        """
        filename = cls.__name__ + '.csv'
        if os.path.exists(filename):
            with open(filename, 'r') as csvfile:
                reader = csv.reader(csvfile)
                instances = []
                for row in reader:
                    if cls.__name__ == 'Rectangle':
                        dictionary = {"id": int(row[0]),
                                      "width": int(row[1]),
                                      "height": int(row[2]),
                                      "x": int(row[3]),
                                      "y": int(row[4])}
                    elif cls.__name__ == 'Square':
                        dictionary = {"id": int(row[0]),
                                      "size": int(row[1]),
                                      "x": int(row[2]),
                                      "y": int(row[3])}
                    instance = cls.create(**dictionary)
                    instances.append(instance)
                return instances
        return []

    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.
        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()        
