#!/usr/bin/python3

__name__ == "__main__"
from calculator_1 import add, sub, mul, div

a = 10
b = 5

print(f"{a} + {b} = {add(a, b)}"'\n'f"{a} - {b} = {sub(a, b)}"'\n'f"{a} * {b} = {mul(a, b)}"'\n'f"{a} / {b} = {div(a, b)}")
