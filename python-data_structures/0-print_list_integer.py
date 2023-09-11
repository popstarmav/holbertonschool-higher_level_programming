#!/usr/bin/python3

def print_list_integer(my_list=[]):
    # Print all integers of a list.
    for nun in my_list:
        if isinstance(nun, int):
            print("{:d}".format(nun))
