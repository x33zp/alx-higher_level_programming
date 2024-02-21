#!/usr/bin/python3
"""
Contains function write_file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)

    Returns:
            number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
