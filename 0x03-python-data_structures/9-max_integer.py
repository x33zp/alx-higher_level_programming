#!/usr/bin/python3
def max_integer(my_list=[]):
    '''finds the biggest integer of a list.'''
    max_int = my_list[0] if len(my_list) else None

    for i in my_list:
        if i > max_int:
            max_int = i
    return max_int
