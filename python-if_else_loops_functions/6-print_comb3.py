#!/usr/bin/python3
# 6-print_comb3.py

for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 8 and digit2 == 9:
            print("{:d}{:d}".format(digit1, digit2))
        else:
            print("{:d}{:d}, ".format(digit1, digit2), end="")

