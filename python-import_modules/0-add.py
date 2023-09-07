#!/usr/bin/python3

# Import the add function from the add_0 module
from add_0 import add

# Assign the values to variables a and b
a = 1
b = 2

# Perform the addition and print the result using string formatting
result = add(a, b)
print("{} + {} = {}".format(a, b, result))
