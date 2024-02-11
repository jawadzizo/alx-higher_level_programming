#!/usr/bin/python3
"""Module for the BaseGeometry and Rectangle classes
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """the Rectangle class"""

    def __init__(self, width, height):
        """the constructor method"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
