#!/usr/bin/python3
"""Return json of a string"""
import json



def to_json_string(my_obj):
    """Converts object to JSON string."""
    data = json.dumps(my_obj) 
    return data
