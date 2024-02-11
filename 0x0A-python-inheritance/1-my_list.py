#!/usr/bin/python3
"""Module that prints a sorted list
"""


class MyList(list):
    """a subclass of the list class"""

    def print_sorted(self):
        """prints a sorted list"""

        print(sorted(self))
