#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        item_count = 0
        for i in range(0, x):
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                item_count += 1
        print("")
        return item_count
    except (TypeError, ValueError):
        print("")
        return item_count
