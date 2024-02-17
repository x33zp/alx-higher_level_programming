#!/usr/bin/python3
"""Indents text"""


def text_indentation(text):
    """
    a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punc = {'.', ':', '?'}

    charID = 0
    for char in text:
        if charID == 0:
            if char == ' ':
                continue
            else:
                charID= 1

        if charID == 1:
            if char in punc:
                print(char)
                print()
                breakP = 0
            else:
                print(char, end="")
