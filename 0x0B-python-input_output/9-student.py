#!/usr/bin/python3
"""
Contains a class Student
"""


class Student:
    """A class used to represent a Student"""

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the given first name,
        last name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        This method returns the dictionary representation of the instance's
        attributes, making it easy to serialize the student's information,
        for example, when storing or transmitting the data.

        Returns:
            A dictionary containing the student's first name,last name,
            and age.
        """
        return self.__dict__
