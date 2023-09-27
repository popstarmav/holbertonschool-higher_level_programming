#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file
"""
import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

# Load the existing list from "add_item.json" (if it exists)
try:
    existing_list = load_from_json_file("add_item.json")
except:
    existing_list = []

# Add command-line arguments to the list
existing_list.extend(sys.argv[1:])

# Save the updated list to "add_item.json"
save_to_json_file(existing_list, "add_item.json")
