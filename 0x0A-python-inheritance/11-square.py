#!/usr/bin/python3
""" Module with Square class """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Rectangle """
    def __init__(self, size):
        """ Constructor """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Compute area """
        return self.__size ** 2

    def __str__(self):
        """ Prints string """
        return "[Square] {}/{}".format(self.__size, self.__size)
