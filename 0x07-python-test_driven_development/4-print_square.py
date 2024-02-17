#!/usr/bin/python3
def print_square(size):
    """a function that prints a square swith the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    print("\n".join(["#" * size] * size))
