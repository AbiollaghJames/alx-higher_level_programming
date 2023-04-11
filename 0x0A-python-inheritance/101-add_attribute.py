#!/usr/bin/python3
""" Module with add_attribute function """


def add_attribute(obj, name, val):
    """ adds attribute """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, val)
