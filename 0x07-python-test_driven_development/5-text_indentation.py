#!/usr/bin/python3
"""
indents a string passed to it
"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of these characters:
    '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punc = {'.', ':', '?'}

    count = 0
    for ch in text:
        if count == 0:
            if ch == ' ':
                continue
            else:
                count = 1
        if count == 1:
            if ch in punc:
                print(ch)
                print()
                count = 0
            else:
                print(ch, end="")
