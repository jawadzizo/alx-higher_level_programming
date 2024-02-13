#!/usr/bin/python3
""" Module of the Base class to be used as parent class for other classes
"""


class Base():
    """The base class of other subclass"""

    __nb_objects = 0

    def __init__(self, id=None):
        """The constructor method of Base class's instances"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of list_dictionaries"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []

        import json

        return json.dumps(list_dictionaries)
