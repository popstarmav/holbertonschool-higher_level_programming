#!/usr/bin/python3
"""
say_my_name function prints back :
    <first_name><lastname>
"""
def say_my_name(first_name, last_name=""):
    """
    check if first_name is a string 
    check if last_name is a string
    """
    if not (type(first_name) is str):
        raise TypeError("first_name must be a string")

    if not (type(last_name) is str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
