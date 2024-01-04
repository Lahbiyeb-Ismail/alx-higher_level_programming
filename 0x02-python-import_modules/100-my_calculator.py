#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv_len = len(argv) - 1
    if argv_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = argv[2]
    if operator != "+" and operator != "-" and operator != "*" and operator != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, div, mul, sub

    a = int(argv[1])
    b = int(argv[3])
    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    if operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    if operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    if operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))
