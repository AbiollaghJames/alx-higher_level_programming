#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """define class Rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrive width"""
        return self.__width

    @property
    def height(self):
        """retrieve height"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

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
        """compute area"""
        return self.__width * self.__height

    def perimeter(self):
        """compute perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))
