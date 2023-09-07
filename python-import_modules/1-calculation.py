#!/usr/bin/python3

# Import functions from calculator_1.py
from calculator_1 import add, sub, mul, div

# Define the values
a = 10
b = 5

# Perform calculations and print results
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
