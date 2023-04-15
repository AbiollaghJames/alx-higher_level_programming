#!/usr/bin/python3
""" Module with the class Square """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ class Square """

    def __init__(self, size, x=0, y=0, id=None):
        """ a constructor """

        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size

    def __str__(self):
        """ print string rep of square """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ get size """
        return self.width

    @size.setter
    def size(self, value):
        """ set size """
        self.width = value
        self.height = value
