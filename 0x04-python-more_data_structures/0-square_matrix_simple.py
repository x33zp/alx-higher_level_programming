#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Computes the square value of all integers of a matrix'''
    new_matrix = [list(map(lambda x: x**2, i)) for i in matrix]
    return new_matrix
            
