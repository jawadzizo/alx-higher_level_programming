#!/usr/bin/python3
"""A module to write to a file"""


def write_file(filename="", text=""):
    """write to a file and returns the number of written characters"""
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(str(text)))
