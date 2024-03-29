#!/usr/bin/python3
""" continue practice with classes!!! """


class Rectangle:
    """ initialize the width and height with value checks

    Args:
        width: how fat is this 4 polygon gonna be
        height: how tall is this box

    Return: nonezo
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ calculates the area of this rect """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of this rect """
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width) * 2 + (self.__height * 2)

    def __str__(self):
        string = ""
        if self.__width is 0 or self.__height is 0:
            return string
        for e in range(self.__height):
            for f in range(self.__width):
                string += "#"
            if e is not self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
