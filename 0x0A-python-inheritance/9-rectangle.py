#!/usr/bin/python3
"""Module for the Rectangle class
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

    def area(self):
        """returns the area of the rectangle"""

        return self.__height * self.__width

    def __str__(self):
        """returns a string in the format: [Rectangle] <width>/<height>"""

        return (f"[Rectangle] {self.__width}/{self.__height}")
