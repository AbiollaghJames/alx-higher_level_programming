#!/usr/bin/python3
""" module with MyInt class """


class MyInt(int):
    """ class MyInt inherits from int """

    def __eq__(self, obj):
        """ Checks for equality """
        return False

    def __ne__(self, obj):
        """ Return True if not equal """
        return True
