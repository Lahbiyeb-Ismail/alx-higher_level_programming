#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""

    for i in range(0, len(str)):
        if i != n:
            strcpy += str[i]

    return strcpy
