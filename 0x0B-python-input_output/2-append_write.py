#!/usr/bin/python3
"""
Contains function append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)

    Returns:
            number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
