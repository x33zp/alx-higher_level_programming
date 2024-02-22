#!/usr/bin/python3
"""
Defines a class MyInt
"""


class MyInt(int):
    """
    A class representing a rebellious integer.

    This class inherits from int but inverts the behavior of the equality
    and inequality operators.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to return the inverse of the
        int's equality check.

        Parameters:
            other (Any): The value to compare with.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to return the inverse of the
        int's inequality check.

        Parameters:
            other (Any): The value to compare with.

        Returns:
            bool: True if equal, False otherwise.
        """
        return not super().__ne__(other)
