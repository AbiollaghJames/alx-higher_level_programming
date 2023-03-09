#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ope = sys.argv[2]
    if ope != '+' and ope != '-' and ope != '*' and ope != '/':
        print("Unknown operator. Available operators: +, -, * and /")

    from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if ope == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif ope == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif ope == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
