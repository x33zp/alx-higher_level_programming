#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided"""


import math


class MagicClass:
    """
    A class that represents a magic circle.

    Attributes:
        __radius (int or float): The radius of the magic circle.
    """

    def__init__(self, radius=0):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the magic circle. Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        if ot isinstance(radius, (int, float)):
            TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
