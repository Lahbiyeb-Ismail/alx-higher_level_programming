#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_weight = 0
    div = 0

    for tup in my_list:
        total_weight += tup[0] * tup[1]
        div += tup[1]

    return total_weight / div
