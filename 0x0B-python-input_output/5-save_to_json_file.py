#!/usr/bin/python3
""" Module with save_to_json_fie function """
import json


def save_to_json_file(my_obj, filename):
    """ save object to text file using JSON rep """
    with open(filename, "w") as jsonFile:
        json.dump(my_obj, jsonFile)
