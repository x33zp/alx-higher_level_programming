#!/usr/bin/python3
"""
Contains the definition of the class Student.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance with the provided name and age.

        The Student object will contain three main attributes: first_name,
        last_name, and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        dict_rep = {k: v for k, v in self.__dict__.items() if k in attrs}
        return dict_rep
