#!/usr/bin/python3
""" Module with Student class """


class Student:
    """ Defines Student """
    def __init__(self, first_name, last_name, age):
        """ Student class constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve a dict rep of class Student """
        if (type(attrs) == list and all(type(elem) == str for elem in attrs)):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__
