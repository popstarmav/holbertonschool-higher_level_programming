#!/usr/bin/python3

def print_list_integer(my_list=[]):
    if isinstance(my_list, list):
        for num in my_list:
            print("{:d}".format(num))
