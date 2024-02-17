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
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in punc:
            lines.append(current_line.strip())
            current_line = ""

    for line in lines:
        print(line)
        print()

    if current_line:
        print(current_line.strip())
