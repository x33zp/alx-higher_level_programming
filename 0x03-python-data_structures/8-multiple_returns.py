#!/usr/bin/python3
def multiple_returns(sentence):
    '''returns a tuple with the length of a string and its first character.'''
    if len(sentence) > 0:
        return len(sentence), sentence[0]
    else:
        return None
