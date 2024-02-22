#!/usr/bin/python3
"""
Contains function def append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line containing a specific string
    in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after each line containing
        the search string.
    """
    with open(filename, 'r') as file:
        line_list = []

        for line in file:
            line_list.append(line)

            if search_string in line:
                line_list.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(line_list)
