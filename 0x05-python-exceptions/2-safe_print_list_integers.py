#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_items = 0

    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end="")
            printed_items += 1
        except (ValueError, TypeError):
            continue

    print()
    return (printed_items)
