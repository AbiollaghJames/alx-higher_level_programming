#!/usr/bin/python3
""" Model with class Recatngle """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ get width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ get height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ get x """
        return self.__x

    @x.setter
    def x(self, value):
        """ set x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get y """
        return self.__y

    @y.setter
    def y(self, value):
        """ set y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ return area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ prints # pattern of the rectangle """
        for i in range(self.__y):
            print()

        for j in range(self.__height):
                print(' ' * self.__x, end="")

                for k in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        """ prints string rep of the rectangle """
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(type(self).__name__, self.id, self.__x, self.__y, self.__width, self.__height)

    def to_dictionary(self):
        """ returns dict rep of a class """
        my_dict = {"id": 0, "width": 0, "height": 0, "x": 0, "y": 0}

        for key in my_dict:
            if key == "id":
                my_dict[key] = self.id
            elif key == "width":
                my_dict[key] = self.width
            elif key == "height":
                my_dict[key] = self.height
            elif key == "x":
                my_dict[key] = self.x
            elif key == "y":
                my_dict[key] = self.y

            return my_dict

    def update(self, *args, **kwargs):
        """ assign args to eah attribute """
        if args is not None and len(args) != 0:
            for arg in range(len(args)):
                if arg == 0:
                    self.id = args[arg]
                elif arg == 1:
                    self.__width = args[arg]
                elif arg == 2:
                    self.__height = args[arg]
                elif arg == 3:
                    self.__x = args[arg]
                elif arg == 4:
                    self.__y = args[arg]

        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.__width = kwargs[key]
                elif key == "height":
                    self.__height = kwargs[key]
                elif key == "x":
                    self.__x = kwargs[key]
                elif key == "y":
                    self.__y = kwargs[key]
