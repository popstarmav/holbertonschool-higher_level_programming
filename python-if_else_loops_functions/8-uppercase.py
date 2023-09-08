#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        # Check for lowercase letter
        if 'a' <= char <= 'z':
            # Convert lowercase to uppercase
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
        else:
            uppercase_char = char
        result += uppercase_char
    print("{}".format(result))
