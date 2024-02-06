#!/usr/bin/python3
"""A module to return an object from a JSON string"""

import json


def from_json_string(my_str):
    """returns an object from a JSON string"""
    return (json.loads(my_str))
