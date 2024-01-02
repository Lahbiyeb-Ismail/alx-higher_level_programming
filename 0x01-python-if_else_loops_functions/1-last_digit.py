#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = str(number)[-1]
output_str = "Last digit of " + str(number) + " is " + last_digit;

if int(last_digit) > 5:
	output_str += " and is greater that 5"
elif int(last_digit) == 0:
	output_str += " and is 0"
else:
	output_str += " and is less than 6 and not 0"

print(output_str)
