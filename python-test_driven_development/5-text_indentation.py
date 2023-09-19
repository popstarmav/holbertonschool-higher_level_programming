#!/usr/bin/python3
"""
 function that prints a text with 2 new lines
 after each of these character : ['.', '?', ':']
"""
def text_indentation(text):
    """define varibales and methods"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars_to_split = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if char in chars_to_split:
            lines.append(current_line.strip())
            current_line = ""

    # Add the last line if it's not empty
    if current_line:
        lines.append(current_line.strip())

    for line in lines:
        print(line)
        print()
