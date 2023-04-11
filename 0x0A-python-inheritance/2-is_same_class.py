#!/usr/bin/python3
"""
This module contains is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is instatnce of class else False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
