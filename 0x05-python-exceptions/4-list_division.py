#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    idx = 0
    results_arr = []

    while idx < list_length:
        res = 0

        try:
            res = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            results_arr.append(res)
            idx += 1

    return results_arr
