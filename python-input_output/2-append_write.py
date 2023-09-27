#!/usr/bin/python3
"""
Function appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Append text to the file and return the character count"""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            num_chars_added = file.write(text)
        return num_chars_added
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
