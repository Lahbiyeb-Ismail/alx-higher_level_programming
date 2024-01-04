#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    from calculator_1 import add, div, mul, sub

    argv_len = len(argv) - 1
    if argv_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if operator == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operator == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operator == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
