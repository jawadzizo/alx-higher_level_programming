#!/usr/bin/python3
"""checks if 'obj' is an instance of a class that inherited 'a_class'
"""


def inherits_from(obj, a_class):
    """checks if 'obj' is an instance of a class that inherited 'a_class'"""

    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
