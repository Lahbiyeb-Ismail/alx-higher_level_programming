#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list.copy())
    result = 0
    for num in my_set:
        result += num

    return result


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
