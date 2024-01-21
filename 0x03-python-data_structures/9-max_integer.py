#!/usr/bin/python3
def max_integer(my_list=[]):
    '''finds the biggest integer of a list.'''
    max = my_list[0] if len(my_list) else None
    for i in my_list:
        if i > max:
            max = i
    return max
