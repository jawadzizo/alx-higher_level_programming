#!/usr/bin/python3
"""
A module for dividing a matrix elements by a given number
the matrix should only contain integers or floats
the matrix should only contain rows of same size
the number to divide with should be either an integer or float,\
and must not be 0
a new matrix should be returned, with 2 digits after the dot
"""


def matrix_divided(matrix, div):
    """
    divides the elements of matrix by div
    """

    matrix_type = "matrix must be a matrix (list of lists) of integers/floats"
    matrix_size = "Each row of the matrix must have the same size"

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not isinstance(matrix[0], list):
        raise TypeError(matrix_type)

    size = len(matrix[0])
    new = []

    for row in matrix:
        if isinstance(row, list) is False:
            raise TypeError(matrix_type)

        if len(row) != size:
            raise TypeError(matrix_size)

        temp = []

        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(matrix_type)

            temp.append(round(float(element / div), 2))

        new.append(temp)

    return (new)
