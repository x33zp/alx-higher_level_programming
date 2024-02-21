#!/usr/bin/python3
"""
Contains function read_file
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
