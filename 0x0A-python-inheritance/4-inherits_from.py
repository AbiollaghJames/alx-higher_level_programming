#!/usr/bin/python3
"""
The module with inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is instance of class (directly/indirectly)
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
