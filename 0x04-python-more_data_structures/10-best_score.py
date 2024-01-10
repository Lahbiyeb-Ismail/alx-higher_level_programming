#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        max_val = -999999
        best_key = ""
        for key, val in a_dictionary.items():
            if val > max_val:
                max_val = val
                best_key = key

        return best_key
