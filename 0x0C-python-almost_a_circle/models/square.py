#!/usr/bin/python3
""" Module of the Square class that inherits from the Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """The constructor method for Square class's instances"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints the square in format: [Square] (<id>) <x>/<y> - <size>"""

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """the getter method of size attribute"""

        return self.width

    @size.setter
    def size(self, size):
        """the setter method of size attribute"""

        self.width = size
        self.height = size
