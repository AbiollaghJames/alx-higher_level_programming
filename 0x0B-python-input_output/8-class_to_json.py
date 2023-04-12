#!/usr/bin/python3
""" Module with class_to_json function """


def class_to_json(obj):
    """ Returns dict description class """
    return (getattr(obj, "__dict__"))
