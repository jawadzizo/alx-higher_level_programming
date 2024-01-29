#!/usr/bin/python3
"""a file containing all methods and fields of the class \"Square\""""


class Square:
    """the 6th version of the class \"Square\""""

    def __init__(self, size=0):
        """the __init__ method to define some object fields"""
        self.size = size

    @property
    def size(self):
        """a size property that returns the original size"""
        return self.__size

    @size.setter
    def size(self, value):
        """"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """a method that returns the square of the object size"""
        return (self.__size ** 2)

    def my_print(self):
        """a method that prints the square using '#'"""
        for i in range(self.__size):
            print("#" * self.__size)

        if self.__size == 0:
            print("")
