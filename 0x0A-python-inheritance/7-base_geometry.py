#!/usr/bin/python3
"""Module for the BaseGeometry class
"""


class BaseGeometry:
    """the BaseGeometry class"""

    def area(self):
        """raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is a positive integer"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
