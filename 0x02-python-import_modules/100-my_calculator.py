#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    from calculator_1 import add, div, mul, sub

    argv_len = len(argv) - 1

    if argv_len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operations = {"+": add, "-": sub, "*": mul, "/": div}
    operator = argv[2]

    if operator not in list(operations.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, operator, b, operations[operator](a, b)))
