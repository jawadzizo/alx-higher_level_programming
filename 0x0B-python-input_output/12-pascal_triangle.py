#!/usr/bin/python3
"""A module that returns a Pascal Triangle using a nested list"""


def pascal_triangle(n):
    """returns a Pascal Triangle using a nested list"""

    pascal = []
    length = 1

    if isinstance(n, int) is False or n <= 0:
        return (pascal)

    for i in range(n):
        array = []

        for j in range(length):

            if i == 0 or len(array) == 0 or len(array) == len(pascal[i - 1]):
                element = 1
            else:
                element = pascal[i-1][len(array)] + pascal[i-1][len(array) - 1]

            array.append(element)

        length += 1
        pascal.append(array)

    return (pascal)
