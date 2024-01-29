#!/usr/bin/python3
"""a file containing all methods and fields of the class \"Rectangle\""""


class Rectangle:
    """the 2nd version of the class \"Rectangle\""""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the Rectangle class"""
        return self.__width

    @property
    def height(self):
        """returns the height of the Rectangle class"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the rectangle's width after validating some conditions"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the rectangle's height after validating some conditions"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
