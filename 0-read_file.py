#!/usr/bin/python3
"""
function read and prints 
it to stdout
"""

def read_file(filename=""):
    try:
        # Open the file for reading with UTF-8 encoding
        with open(filename, 'r', encoding='utf-8') as file:
            # Read and print each line in the file
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        pass
