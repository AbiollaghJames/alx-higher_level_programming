#!/usr/bin/python3
"""
The module with inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is instance of class (directly/indirectly)
    """

    if isinstance(obj, a_class):
        return True
    elif type(obj) is a_class:
        return False
