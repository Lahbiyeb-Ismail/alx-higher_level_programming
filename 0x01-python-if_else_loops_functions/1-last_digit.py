#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
sign = 1

if number < 0:
    sign = -1
else:
    sign = 1

last_digit = str(number)[-1]

if sign == -1 and last_digit != "0":
    last_digit = int(last_digit) * sign
else:
    last_digit = int(last_digit) * sign

output_str = "Last digit of " + str(number) + " is " + str(last_digit)

if last_digit > 5:
    output_str += " and is greater than 5"
elif last_digit == 0:
    output_str += " and is 0"
else:
    output_str += " and is less than 6 and not 0"

print(output_str)
