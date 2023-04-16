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

    def update(self, *args, **kwargs):
        """ assigns attributes """
        if args is not None and len(args) != 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                elif arg == 1:
                    self.width = args[arg]
                    self.height = args[arg]
                elif arg == 2:
                    self.x = args[arg]
                elif arg == 3:
                    self.y = args[arg]

        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]
