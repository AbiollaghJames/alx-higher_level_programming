#!/usr/bin/python3
"""Module with write_file function"""


def write_file(filename="", text=""):
    """ writes to tet file and return number of characters"""
    with open(filename, "w", encoding="UTF-8") as myFile:
        myFile.write(text)

        for char in text:
            char += 1

        return char
