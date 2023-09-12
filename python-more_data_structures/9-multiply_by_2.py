#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    result_dictionary = {}

    # Iterate through the original dictionary and multiply values by 2
    for key, value in a_dictionary.items():
        result_dictionary[key] = value * 2

    return result_dictionary
