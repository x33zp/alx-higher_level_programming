#!/usr/bin/python3
"""
Contains function matrix_mul
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix to be multiplied.
                             Each sublist represents a row.
                             Must contain only integers or floats.
                             All rows must be of the same size.
        m_b (list of lists): The second matrix to be multiplied.
                             Each sublist represents a row.
                             Must contain only integers or floats.
                             All rows must be of the same size.

    Returns:
        list of lists: The resulting matrix after multiplication.
                       Each sublist represents a row.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of
                   lists, or if any element in the matrices is not
                   an integer or float, or if any row in the matrices
                   is not of the same size.
        ValueError: If m_a or m_b is empty, or if the matrices cannot be
                    multiplied due to incompatible sizes.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not all(row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not all(row for row in m_b):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for number in row:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for number in row:
            if not isinstance(number, int) and not isinstance(number, float):
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")
    if len(m_a[0]) is not len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for i in range(len(m_b[0]))] for i in range(len(m_a))]
    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
