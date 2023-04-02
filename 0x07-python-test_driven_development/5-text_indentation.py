#!/usr/bin/python3
""" text indentation"""


def text_indentation(text):
    """print text with 2 new lines after chars ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0

    for letter in text:
        if flag == 0:

            if letter == ' ':
                continue
            else:
                flag = 1

        if flag == 1:
            if letter == '?' or letter == '.' or letter == ':':
                print(letter)
                print()
                flag = 0

            else:
                print(letter, end="")
