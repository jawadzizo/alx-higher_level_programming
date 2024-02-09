#!/usr/bin/python3
"""
A module for adding 2 integers or floats
a: integer or float
b: integer or float

"""


def add_integer(a, b=98):
    """
    adds to integers or floats, returns an integer
    """

    dic_t = {"a": a, "b": b}

    for k, v in dic_t.items():
        if type(v) not in [int, float]:
            raise TypeError(f"{k} must be an integer")
        if isinstance(v, float):
            dic_t[k] = int(v)

    return (dic_t["a"] + dic_t["b"])
