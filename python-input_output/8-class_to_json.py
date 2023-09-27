#!/usr/bin/python3
"""function that returns the dictionary"""

def class_to_json(obj):
    if hasattr(obj, '__dict__'):
        serializable_dict = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                serializable_dict[key] = value
        return serializable_dict
    else:
        raise TypeError("Object lacks a dictionary representation")
