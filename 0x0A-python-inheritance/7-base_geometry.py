#!/usr/bin/python3
"""Module with BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """computes area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """public integer_validator method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
