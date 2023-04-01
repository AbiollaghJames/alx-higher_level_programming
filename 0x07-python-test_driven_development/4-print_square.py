#!/usr/bin/python3
"""print pattern"""


def print_square(size):
    """print square with character '#'"""

    if type(size) is not int and type(size) is float:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")

            print()
