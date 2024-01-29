#!/usr/bin/python3
"""a file containing all methods and fields of the class \"Rectangle\""""


class Rectangle:
    """the 10th version of the class \"Rectangle\""""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initialize object's value
        also increments instances count"""
        self.width = width
        self.height = height
        self.print_symbol = Rectangle.print_symbol
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns the width of the Rectangle class"""
        return self.__width

    @property
    def height(self):
        """returns the height of the Rectangle class"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the rectangle's width after validating some conditions"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the rectangle's height after validating some conditions"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """returns a formated rectangle using '#'"""

        text = ""
        if self.__width == 0 or self.__height == 0:
            return text
        for i in range(self.__height):
            text += (str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                text += "\n"
        return text

    def __repr__(self):
        """returns a string for eval to create new objects"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """says by when a rectangle is deleted );
        also decrements instances count"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compare 2 objects, returns the biggest one based on area"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """a class method that creates a Square object using Rectanle class"""
        return Rectangle(size, size)
