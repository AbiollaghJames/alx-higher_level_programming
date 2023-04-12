#!/usr/bin/python3
"""Module with read_file function"""


def read_file(filename=""):
    """Reads text file(UTF-8)and print to stdout"""
    with open(filename, "r", encoding="UTF-8") as myFile:
        print(myFile.read())
