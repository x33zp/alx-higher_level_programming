#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    '''deletes keys with a specific value in a dictionary.'''
    for k in dict(a_dictionary):
        if a_dictionary[k] == value:
            del a_dictionary[k]
    return a_dictionary
