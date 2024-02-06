#!/usr/bin/python3
"""A module to append to a file"""


def append_write(filename="", text=""):
    """appends to a file and returns the number of written characters"""
    with open(filename, "a", encoding="utf-8") as f:
        return (f.write(str(text)))
