#!/usr/bin/python3
"""Define a MagicClass matching exactly a bytecode provided"""
import math


class MagicClass:
    """
    A class that represents a magic circle
    """

    def __init__(self, radius=0):
        """
        Initialize a MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the magic circle.
            Defaults to 0.

        Raises:
            TypeError: If radius is not a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculate the area of the magic circle.

        Returns:
            float: The area of the magic circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculate the circumference of the magic circle.

        Returns:
            float: The circumference of the magic circle.
        """
        return 2 * math.pi * self.__radius
