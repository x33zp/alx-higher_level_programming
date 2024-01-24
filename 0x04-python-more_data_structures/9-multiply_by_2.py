#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''returns a new dictionary with all values multiplied by 2'''
    return {i: j*2 for i, j in a_dictionary.items()}
