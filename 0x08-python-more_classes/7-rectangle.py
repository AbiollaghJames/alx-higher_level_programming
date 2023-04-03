#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """defines rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """return area"""
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """prints rectangles string"""
        string = ""
        for row in range(self.__height):
            for col in range(self.__width):
                string += '#'
            if self.__width != 0 and row < (self.__height - 1):
                string += '\n'
        return string

    def __repr__(self):
        """return object func rep of rectangle"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """detects deletion instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
