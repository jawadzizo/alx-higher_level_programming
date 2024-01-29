#!/usr/bin/python3
"""a file containing all methods and fields of the class \"Square\""""


class Square:
    """the 7th version of the class \"Square\""""

    def __init__(self, size=0, position=(0, 0)):
        """the __init__ method to define some object fields"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """a size property that returns the original size"""
        return self.__size

    @property
    def position(self):
        """a position property that returns the original position"""
        return self.__position

    @size.setter
    def size(self, value):
        """a setter method for the size attribute"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """a setter method for the position attribute"""
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for element in value:
            if isinstance(element, int) is False or element < 0:
                raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """a method that returns the square of the object size"""
        return (self.__size ** 2)

    def my_print(self):
        """a method that prints the square using '#'"""
        if self.__size != 0:
            print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)

        else:
            print("")

    def __str__(self):
        """prints the square in a nice format"""
        text = ""
        if self.__size != 0:
            text += ("\n" * self.__position[1])
            for i in range(self.__size):
                text += (" " * self.__position[0])
                text += ("#" * self.__size)
                if i != self.__size - 1:
                    text += "\n"

        else:
            text = "\n"

        return text
