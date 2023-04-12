#!/usr/bin/python3
""" Module with append_file function """


def append_write(filename="", text=""):
    """ append string at end of a file """
    with open(filename, "a", encoding="UTF-8") as myFile:
        myFile.write(text)

        return len(text)
