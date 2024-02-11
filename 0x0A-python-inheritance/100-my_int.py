#!/usr/bin/python3
"""Module that inverts the equality of an integer
"""


class MyInt(int):
    """subclass of the class 'int'"""

    def __eq__(self, value):
        """returns False if self==value"""

        return not super().__eq__(value)

    def __ne__(self, value):
        """returns True if self!=value"""

        return not super().__ne__(value)
