#!/usr/bin/python3
"""Define a class"""


class Square:
    """private instance size, can only be used by self"""
    def __init__(self, size=0):
        self.__size = size
