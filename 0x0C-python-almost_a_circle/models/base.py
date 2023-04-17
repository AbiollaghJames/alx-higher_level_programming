#!/usr/bin/python3
""" Model with class Base """
import json


class Base:
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ class constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ return JSON representation of a dictionary """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write JSON rep of list_objs to file """
        fname = "{:s}.json".format(cls.__name__)
        file_content = []

        if list_objs is not None:
            for i in range(len(list_objs)):
                file_content.append(cls.to_dictionary(list_objs[i]))

        with open(fname, mode="w", encoding="utf-8") as my_file:
            my_file.write(cls.to_json_string(file_content))
