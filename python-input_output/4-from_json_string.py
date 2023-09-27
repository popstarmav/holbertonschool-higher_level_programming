#!/usr/bin/python3
"""data structure"""
import json



def from_json_string(my_str):
    """return obj by json string"""
    data = json.loads(my_str)
    return data
