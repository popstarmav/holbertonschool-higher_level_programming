#!/usr/bin/python3
import random

# Generate a random number
number = random.randint(-10, 10)

if number > 0:
    print(f'The number {number} is positive')
elif number == 0:
    print(f'The number {number} is zero')
else:
    print(f'The number {number} is negative')
