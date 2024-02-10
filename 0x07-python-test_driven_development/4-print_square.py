#!/usr/bin/python3
"""
A module for printing the full name
both arguments must be strings
atleast 1 argument should be passed
return nothing
"""


def print_square(size):
    """
    prints a square by size using '#'
    """

    if isinstance(size, int) is False or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
