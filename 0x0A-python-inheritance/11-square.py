#!/usr/bin/python3
"""Module for the Square class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """the Square class"""

    def __init__(self, size):
        """the constructor method"""

        super().integer_validator("size", size)

        self.__size = size

    def area(self):
        """returns the area of the square"""

        return self.__size * self.__size

    def __str__(self):
        """returns a string in the format: [Rectangle] <size>/<size>"""

        return (f"[Square] {self.__size}/{self.__size}")
