#!/usr/bin/python3
""" 
a function that finds a peak in a list of unsorted integers.
"""

"""
    Initialization of maximum value to None then looping
    through each and every element of the list and comaparing with 
    the maximum element as we keep track of maximum element
    Efficiency -> O(n)
"""
def find_peak(list_of_integers):
    """ Brute force """
    max_value = None

    for val in list_of_integers:
        if max_value is None or max_value < val:
            max_value = val
    return max_value
