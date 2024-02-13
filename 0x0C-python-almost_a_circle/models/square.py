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

    def update(self, *args, **kwargs):
        """updates the attributes of Square's instances"""

        if len(args) > 0:

            attributes = [0, 1, 2, 3]

            attributes[0] = args[0] if len(args) > 0 else self.id
            attributes[1] = args[1] if len(args) > 1 else self.size
            attributes[2] = args[2] if len(args) > 2 else self.x
            attributes[3] = args[3] if len(args) > 3 else self.y

            super().__init__(attributes[1], attributes[1], attributes[2], attributes[3], attributes[0])

        elif len(kwargs) > 0:

            attributes = {}

            attributes["id"] = kwargs["id"] if "id" in kwargs else self.id
            attributes["size"] = kwargs["size"] if "size" in kwargs else self.size
            attributes["x"] = kwargs["x"] if "x" in kwargs else self.x
            attributes["y"] = kwargs["y"] if "y" in kwargs else self.y

            super().__init__(attributes["size"], attributes["size"], attributes["x"], attributes["y"], attributes["id"])
