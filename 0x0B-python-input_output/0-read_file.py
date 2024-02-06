#!/usr/bin/python3
"""A module to read a file"""


def read_file(filename=""):
    """A function that reads the content of a file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
