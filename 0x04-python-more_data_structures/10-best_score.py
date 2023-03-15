#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    big = 0
    for key, value in a_dictionary.items():
        if value > big:
            big = value
    for key, value in a_dictionary.items():
        if value == big:
            return key
