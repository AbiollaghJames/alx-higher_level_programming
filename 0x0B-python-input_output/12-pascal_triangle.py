#!/usr/bin/pytho3
""" Module with pascal_triangle function """


def pascal_triangle(n):
    """ return list of lists rep pascal triangle """
    if n <= 0:
        return []

    pas = [[1]]

    if n >= 2:
        pas.append([1, 1])

    for i in range(n-2):
        x = pas[-1]
        new_list = [1, 1]
        y = 1

        for index in range(0, len(x)-1):
            new_list.insert(y, (x[index] + x[index + 1]))
            y += 1

        pas.append(new_list)

    return (pas)
