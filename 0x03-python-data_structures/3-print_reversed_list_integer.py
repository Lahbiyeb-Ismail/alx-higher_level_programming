#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for idx in reversed(range(0, len(my_list))):
            print("{:d}".format(my_list[idx]))
