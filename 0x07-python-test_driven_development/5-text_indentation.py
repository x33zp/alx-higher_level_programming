#!/usr/bin/python3
"""
Supplies a function that indents text
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    count = 0
    for ch in text:
        if count == 0:
            if ch == ' ':
                continue
            else:
                count = 1
        if count == 1:
            if ch == '?' or ch == '.' or ch == ':':
                print(ch)
                print()
                flag = 0
            else:
                print(ch, end="")
