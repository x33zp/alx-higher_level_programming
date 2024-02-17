#!/usr/bin/python3
"""
Supplies a function that indents text
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: '.', '?' and ':'
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
        if charID == 1:
            if char == '?' or char == '.' or char == ':':
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")
