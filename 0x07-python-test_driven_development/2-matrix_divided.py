#!/usr/bin/python3
"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The matrix to be divided.
            Each row should be a list of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix where each element is the result of
            dividing the corresponding element of the original matrix by div.
            All elements are rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists containing
            only integers or floats, or if div is not a number.
        ZeroDivisionError: If div is equal to zero.
    """
    if not isinstance(matrix, list) or not all(
           isinstance(row, list) and
           all(isinstance(ele, (int, float)) for ele in row)
           for row in matrix):
        raise TypeError(
               "matrix must be a matrix (list of lists) of integers/floats")
    elif any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
