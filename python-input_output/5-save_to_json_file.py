#!/usr/bin/python3
"""function that writes an Object to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """Write Python object as JSON to the specified file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(my_obj, file)
    except Exception as e:
        print(f"An error occurred: {e}")
