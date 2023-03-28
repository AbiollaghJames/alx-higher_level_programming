#!/usr/bin/python3
"""Define clas"""


class Square:
    """define sqr"""

    def __init__(self, size=0, position=(0, 0)):
        """attributes"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve data"""
        return self.__size

    @size.setter
    def size(self, value):
        """alter data"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """retireve data"""
        return self.__position

    @position.setter
    def position(self, value):
        """alter data"""
        if type(value) is tuple and len(value) == 2 and type(value[0]) is int and type(value[1]) is int and value[0] >= 0 and value[1] >= 0:
            self.__position = value

        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """public func"""
        return self.__size * self.__size

    def my_print(self):
        """public func"""
        if self.__size > 0:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print(' ' * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
