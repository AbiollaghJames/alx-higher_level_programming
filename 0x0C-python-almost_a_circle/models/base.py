#!/usr/bin/python3
""" Model with class Base """
import json
import csv

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

    @classmethod
    def from_json_string(json_string):
        """ return lsit of JSON string """
        my_list = []
        if json_string is not None and json_string != "":
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """ return instance with all attributes """
        if cls.__name__ == "Rectangle":
            x = cls(1, 1)
        if cls.__name__ == "Square":
            x = cls(1)
        x.update(**dictionary)
        return x

    @classmethod
    def load_from_file(cls):
        """return list of instance"""
        filename = "{:s}.json".format(cls.__name__)

        try:
            with open(filename, mode="r", encoding="utf-8") as my_file:
                file_cont = my_file.read()

            my_file = cls.from_json_string(file_cont)
            l_inst = []
            for i in range(len(my_list)):
                l_inst.append(cls.create(**my_list[i]))

        except:
            l_inst = []

        return l_inst

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serialize"""
        filename = "{:s}.csv".format(cls.__name__)
        f_cont = []

        for i in range(len(list_objs)):
            f_cont.append(cls.to_dictionary(list_objs[i]))

        with open(filename, 'w') as my_file:
            if cls.__name__ == "Rectnagle":
                f_name = ['id', 'width', 'height', 'x', 'y']
            if cls.__name__ == "Square":
                f_name = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(my_file, f_name=f_name)
            writer.writeheader()
            writer.writerows(f_cont)
