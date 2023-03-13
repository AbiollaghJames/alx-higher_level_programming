#!/usr/bin/python3

def multiple_returns(sentence):
    tuple_len = len(sentence)

    if tuple_len == 0:
        first_char = None
    else:
        first_char = sentence[0]
        return ((tuple_len, first_char))
