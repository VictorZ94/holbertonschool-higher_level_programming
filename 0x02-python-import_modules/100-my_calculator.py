#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    av = sys.argv
    if len(av) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(av[0]))
        exit(1)
    if av[2] == '+':
        print("{} + {} = {}".format(av[1], av[3], add(int(av[1]), int(av[3]))))
    elif av[2] == '-':
        print("{} - {} = {}".format(av[1], av[3], sub(int(av[1]), int(av[3]))))
    elif av[2] == '*':
        print("{} * {} = {}".format(av[1], av[3], mul(int(av[1]), int(av[3]))))
    elif av[2] == '/':
        print("{} / {} = {}".format(av[1], av[3], div(int(av[1]), int(av[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
