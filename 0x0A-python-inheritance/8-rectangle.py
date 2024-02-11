#!/usr/bin/python3
"""Module for the BaseGeometry and Rectangle classes
"""


class BaseGeometry:
    """the BaseGeometry class"""

    def area(self):
        """raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is a positive integer"""

        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """the Rectangle class"""

    def __init__(self, width, height):
        """the constructor method"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
