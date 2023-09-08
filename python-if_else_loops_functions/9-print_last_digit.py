#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number) % 10
    
    # Print the last digit and its return value on one line
    print(number, end="")
    
    # Return the last digit
    return number
