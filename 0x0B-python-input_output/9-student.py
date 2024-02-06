#!/usr/bin/python3
"""A module that returns the dictionary of a class instance"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize instance's attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary of a class instance"""
        return (self.__dict__)
