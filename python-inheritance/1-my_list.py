#!/usr/bin/python3
"""
Mylist inherits from the built-in list class.
"""


class MyList(list):
    """Print the list in ascending sorted order"""
     def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
