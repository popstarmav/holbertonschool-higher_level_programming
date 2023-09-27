#!/usr/bin/python3
"""function that creates an Obj from a “JSON file”"""
import json



def load_from_json_file(filename):
    """Load Python object from JSON file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        pass
