#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = [item for i, item in enumerate(my_list) if i != idx]

    # Print the modified list without the removed item
    print(new_list)
