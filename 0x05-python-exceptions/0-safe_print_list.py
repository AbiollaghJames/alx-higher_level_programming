#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    items_printed = 0

    for items in range(0, x):
        try:
            print(my_list[items], end="")
            items_printed += 1
        except IndexError:
            continue
    print()
    return (items_printed)
