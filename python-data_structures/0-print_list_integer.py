#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for num in my_list:
        if isinstance(num, int):  # Check if the element is an integer
            print("{:d}".format(num))
        else:
            raise TypeError("List should only contain integers")
