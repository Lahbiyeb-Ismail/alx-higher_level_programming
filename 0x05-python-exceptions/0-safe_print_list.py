#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    idx = 0
    item_count = 0
    while idx < x:
        try:
            print("{}".format(my_list[idx]), end="")
            item_count += 1
        except IndexError:
            break
        idx += 1

    print("")
    return item_count
