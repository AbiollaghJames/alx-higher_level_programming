#!/usr/bin/python3
"""define class"""


class Square:
    """define square"""

    def __init__(self, size=0):
        """instance of square"""

        self.size = size

    def area(self):
        """compute area"""

        return self.size ** 2

    def eq(self, to_comp):
        return self.area() == to_comp.area()

    def not_eq(self, to_comp):
        return self.area() != to_comp.area()

    def less(self, to_comp):
        return self.area() < to_comp.area()

    def great_eq(self, to_comp):
        return self.area() >= to_comp.area()

    def great(self, to_comp):
        return self.area() > to_comp.area()

    def less_eq(self, to_comp):
        return self.area() <= to_comp.area()

    @property
    def size(self):
        """Get size"""

        return self.__size

    @size.setter
    def size(self, value):
        """set size"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
