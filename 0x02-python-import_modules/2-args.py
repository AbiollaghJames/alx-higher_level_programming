#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    n = len(args)
    ind = 1

    if n == 0:
        print("{:d} arguments.".format(n))
    elif n == 1:
        print("{:d} argument:".format(n))
    else:
        print("{:d} arguments:".format(n))
        while ind <= n:
            print("{:d}: {:s}".format(ind, sys.argv[ind]))
            ind += 1
