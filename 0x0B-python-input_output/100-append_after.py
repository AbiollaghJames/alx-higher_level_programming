#!/usr/bin/python3
""" Module with append_after function """


def append_after(filename="", search_string="", new_string=""):
    """ insert text after line with given string in file """
    text = ""

    with open(filename)as read:
        for line in read:
            text += line
            if search_string in line:
                text += n_string

    with open(filename, "w") as writen:
        written.write(text)
