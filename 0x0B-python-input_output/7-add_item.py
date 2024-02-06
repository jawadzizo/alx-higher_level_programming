#!/usr/bin/python3
"""A module to interact with json representation with files"""

import json
import sys


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """that creates an Object from a “JSON file”"""

    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))


def main():
    """adds all arguments to a Python list, and then save them to a file"""

    filename = "add_item.json"

    try:
        the_list = load_from_json_file(filename)
    except Exception:
        the_list = []

    for i in range(1, len(sys.argv)):
        the_list.append(sys.argv[i])

    save_to_json_file(the_list, filename)


if __name__ == "__main__":
    main()
