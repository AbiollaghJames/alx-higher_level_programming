#!/usr/bin/python3
""" 
a function that finds a peak in a list of unsorted integers.
"""
def find_peak(list_of_integers):
    """ Brute force """
    max_value = None

    for val in list_of_integers:
        if max_value is None or max_value < val:
            max_value = val
    return max_value
