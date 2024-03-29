#!/usr/bin/python3
""" Class 'MagicClass' to replicate bytecode """
import math


class MagicClass():
    """ Definition of a class """
    def __init__(self, radius=0):
        """ Instantiate a MagicClass object to represent a circle """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Compute the area of a circle """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ Compute the circumference of a circle """
        return 2 * math.pi * self.__radius
