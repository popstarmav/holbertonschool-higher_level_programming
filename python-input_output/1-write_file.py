#!/usr/bin/python3
"""
 function that writes a string to a text file (UTF*)
"""


def write_file(filename="", text=""):
    """
    Write the provided text to the specified file and return the
    number of characters written.

    :param filename: The name of the file to write to.
    :param text: The text to write to the file.
    :return: The number of characters written.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_chars_written = file.write(text)
        return num_chars_written
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0
