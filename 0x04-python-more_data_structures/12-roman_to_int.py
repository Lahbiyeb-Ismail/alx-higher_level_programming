#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    for idx in range(len(roman_string)):
        curr_val = roman_dict[roman_string[idx]]
        next_val = (
            roman_dict[roman_string[idx + 1]] if idx + 1 < len(roman_string) else 0
        )
        if curr_val < next_val:
            result -= curr_val
        else:
            result += curr_val

    return abs(result)
