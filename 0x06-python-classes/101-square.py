#!/usr/bin/python3
"""Define class Square"""


class Square:
    """Define square"""

    def __init__(self, size=0, position=(0, 0)):
        """instance of square"""

        self.size = size
        self.position = position

    def __str__(self):
        """ visual rep of a square
        """

        if self.size:
            return '\n' * self.positioin[1] + '\n'.join([' ' * self.position[0] + '#' * self.size] * self.size)
        return str()

    @property
    def size(self):
        """get size"""

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

    @property
    def position(self):
        """get position"""

        return self.__position

    @position.setter
    def position(self, value):
        """set position"""

        if not (isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], int) and isinstance(value[1], int) and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """compute area"""

        return self.size ** 2

    def my_print(self):
        """print visual rep"""

        print(self)
