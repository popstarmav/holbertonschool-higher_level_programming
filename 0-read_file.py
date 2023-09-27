#!/usr/bin/python3
"""
function read and prints 
it to stdout
"""

def read_file(filename=""):
    try:
        file = open(filename, 'r', encoding='utf-8')
        while True:
            line = file.readline()
            if not line:
                break
            print(line, end='')
        file.close()
    except FileNotFoundError:
        passs
