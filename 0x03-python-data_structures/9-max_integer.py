#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = -999999
    if my_list:
        for i in range(len(my_list)):
            if my_list[i] > max_int:
                max_int = my_list[i]
        return max_int
    else:
        return None
