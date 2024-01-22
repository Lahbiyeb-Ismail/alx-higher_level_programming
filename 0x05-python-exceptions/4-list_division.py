#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = 0
    results_arr = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            results_arr.append(result)
        except ZeroDivisionError:
            print("division by 0")
            results_arr.append(0)
        except IndexError:
            print("out of range")
            results_arr.append(0)
        except (TypeError, ValueError):
            print("wrong type")
            results_arr.append(0)

    return results_arr
