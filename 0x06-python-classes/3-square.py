#!/usr/bin/python3
"""a file containing all methods and fields of the class \"Square\""""


class Square:
    """the 4th version of the class \"Square\""""
    def __init__(self, size=0):
        """the __init__ method to define some object fields"""

        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """a method that returns the square of the object size"""
        return (self.__size ** 2)
