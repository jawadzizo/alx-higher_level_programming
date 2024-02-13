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
            return "[]"

        import json

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation to a file"""

        import json
        j_list = []

        for item in list_objs:
            j_list.append(json.loads(Base.to_json_string(item.to_dictionary())))

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(j_list, f)

    @staticmethod
    def from_json_string(json_string):
        """returns an object from a json representation"""

        if json_string is None or len(json_string) == 0:
            return []

        import json

        objects = json.loads(json_string)

        return objects
