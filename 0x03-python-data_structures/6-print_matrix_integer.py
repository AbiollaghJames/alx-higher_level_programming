#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        r_len = len(row)

        for i in range(r_len):
            if i != r_len - 1:
                print("{:d}".format(row[i]), end=' ')
            else:
                print("{:d}".format(row[i]), end='')
        print()
