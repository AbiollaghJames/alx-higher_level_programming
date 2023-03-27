#!/usr/bin/pytho3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:
        sys.stderr.write("Error")
