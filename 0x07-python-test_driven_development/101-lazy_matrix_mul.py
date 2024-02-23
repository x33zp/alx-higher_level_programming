#!/usr/bin/python3
"""
contains function lazy_matrix
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Calculates the matrix multiplication of two matrices.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of matrix multiplication.

    """
    return np.matmul(m_a, m_b)
