#!/usr/bin/python3
"""Module with Rectangle class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle inherits from BaseGometry"""

    def __init__(self, width, height):
        """constructor"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
