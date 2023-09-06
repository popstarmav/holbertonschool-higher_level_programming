#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit

print("Last digit of {} is {} and is ".format(number, last_digit), end="")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
