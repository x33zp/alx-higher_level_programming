#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """splits a text into lines along "?", ":", "." followed by 2 new lines"""
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
