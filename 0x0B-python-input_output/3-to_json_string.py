#!/usr/bin/python3
""" Module to_json_string function """
import json


def to_json_string(my_obj):
    """ returns JSON rep of an object(string) """
    return json.dumps(my_obj)
