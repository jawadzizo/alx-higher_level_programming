#!/usr/bin/python3
"""a file containing all methods and fields of the class \"Rectangle\""""


class Rectangle:
    """the 6th version of the class \"Rectangle\""""
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

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns a formated rectangle using '#'"""
        text = ""
        if self.__width == 0 or self.__height == 0:
            return text
        for i in range(self.__height):
            text += ("#" * self.__width)
            if i != self.__height - 1:
                text += "\n"
        return text

    def __repr__(self):
        """returns a string for eval to create new objects"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """says by when a rectangle is deleted );"""
        print("Bye rectangle...")
