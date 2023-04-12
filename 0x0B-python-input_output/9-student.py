#!/usr/bin/python3
""" Module with Student class """


class Student:
    """ Defines student """
    def __init__(self, first_name, last_name, age):
        """ class Student constructor """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ get dict rep of class Student """
        return (self.__dict__)
