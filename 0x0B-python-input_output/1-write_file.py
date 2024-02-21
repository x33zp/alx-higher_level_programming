#!/usr/bin/python3
"""
Contains function write_file
"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
