#!/usr/bin/python3
""" Module of the Rectangle class that inherits from the Base class
"""


from models.base import Base


class Rectangle(Base):
    """The Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """The constructor method for Rectangle class's instances"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

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

        if isinstance(width, int) is False or isinstance(width, bool):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """The getter method of height attribute"""

        if isinstance(height, int) is False or isinstance(height, bool):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """The getter method of x attribute"""

        if isinstance(x, int) is False or isinstance(x, bool):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        """The getter method of y attribute"""

        if isinstance(y, int) is False or isinstance(y, bool):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y

    def area(self):
        """returns the area of the rectangle"""

        return (self.__width * self.__height)
