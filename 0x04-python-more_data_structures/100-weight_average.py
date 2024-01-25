#!/usr/bin/python3
def weight_average(my_list=[]):
    '''returns the weighted average of all integers tuple'''
    if my_list:
        total = 0
        last_int_sum = 0
        for i in my_list:
            product = i[0] * i[1]
            total += product
            last_int_sum += i[-1]
        result = total / last_int_sum
        return result
