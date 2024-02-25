#!/usr/bin/python3
"""
This module defines the Rectangle class,
which represents a rectangle.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
         Initializes a rectangle with the given width, height,
         x, y, and id.

        Parameters:
        - width: The width of the rectangle.
        - height: The height of the rectangle.
        - x: The x-coordinate of the top-left corner
        of the rectangle (default 0).
        - y: The y-coordinate of the top-left corner
        of the rectangle (default 0).
        - id: Optional. (default None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x attribute.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer.")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y attribute.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y attribute.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer.")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def display(self):
        """
        Display the rectangle using '#' characters,
        considering the x and y coordinates.
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(' ' * self.__x + '#' * self.__width)

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Format:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__,
                                                self.id, self.__x,
                                                self.__y, self.__width,
                                                self.__height)
