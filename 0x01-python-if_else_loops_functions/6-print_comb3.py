#!/usr/bin/python3
'#6-print_com3.py'

for dig in range(0, 10):
    for dig1 in range(dig + 1, 10):
        if dig == 8 and dig1 == 9:
            print("{}{}".format(dig, dig1))
        else:
            print("{}{}".format(dig, dig1), end=", ")
