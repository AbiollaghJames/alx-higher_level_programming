#!/usr/bin/python3
""" Module with load_from_json_file function """
import json


def load_from_json_file(filename):
    """ creates object from a JSON file """
    with open(filename) as objFile:
        return json.load(objFile)
