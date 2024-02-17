#!/usr/bin/python3
"""Indents text"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    charID = 0
    for char in text:
        if charID == 0:
            if char == ' ':
                continue
            else:
                charID = 1
        elif charID == 1:
            if char == ':' or char == '.' or char == '?':
                print(char)
                print()
                breakP = 0
            else:
                print(char, end="")
