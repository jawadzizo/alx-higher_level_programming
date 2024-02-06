#!/usr/bin/python3
"""A module that returns the dictionary of a class instance"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialize instance's attributes"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary of a class instance based on given attrs"""

        if attrs is None:
            return (self.__dict__)

        dictionary = dict()
        self_dict = self.__dict__

        for k, v in self_dict.items():
            if k in attrs:
                dictionary[k] = self_dict[k]

        return (dictionary)
