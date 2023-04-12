#!/usr/bin/python3
""" Module with Student class """


class Student:
    """ Defines Student """
    def __init__(self, first_name, last_name, age):
        """ Constructor """
        self.first_name = first_name
        self.llast_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dict rep of class """
        if (type(attrs) == list and
                all(type(elem) == str for elem in attrs)):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ replace all attr of a class """
        for key, value in json.items():
            setattr(self, key, value)
