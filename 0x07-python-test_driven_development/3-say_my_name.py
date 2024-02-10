#!/usr/bin/python3
"""
A module for printing the full name
both arguments must be strings
atleast 1 argument should be passed
return nothing
"""


def say_my_name(first_name, last_name=""):
    """
    prints the full name
    """

    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
