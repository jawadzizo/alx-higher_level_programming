#!/usr/bin/python3
""" Module of the Rectangle class that inherits from the Base class
"""


from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor method for Rectangle class's instances"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if id is None:
            super().__init__()
        else:
            self.id = id

    @property
    def width(self):
        """The getter method of width attribute"""
        return self.__width

    @property
    def height(self):
        """The getter method of height attribute"""
        return self.__height

    @property
    def x(self):
        """The getter method of x attribute"""
        return self.__x

    @property
    def y(self):
        """The getter method of y attribute"""
        return self.__y

    @width.setter
    def width(self, width):
        """The setter method of width attribute"""
        self.__width = width

    @height.setter
    def width(self, height):
        """The getter method of height attribute"""
        self.__height = height

    @x.setter
    def width(self, x):
        """The getter method of x attribute"""
        self.__x = x

    @y.setter
    def width(self, y):
        """The getter method of y attribute"""

        self.__y = y
