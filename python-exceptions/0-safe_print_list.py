#!/usr/bin/python3
"""
This function print the element of
"""


def safe_print_list(my_list=[], x=0):
    """ defines methods and variables """

    try:
        if x < 0:
            x = 0

        count = 0
        for item in my_list:
            if count < x:
                print(item, end=" ")
                count += 1
            else:
                break

        print()

        return count

    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

my_list = [1, 2, 3, 4, 5]
x = 3
printed_count = safe_print_list(my_list, x)
print(f"Printed {printed_count} elements")
