#!/usr/bin/python3
"""Define a class"""


class Square:
    """private instance attribute size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be a iteger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
