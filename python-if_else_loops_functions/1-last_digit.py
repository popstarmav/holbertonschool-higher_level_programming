#!/usr/bin/python3
import random

# Generate a random signed number between -10000 and 10000
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = abs(number) % 10

# Determine the message based on the last digit
if last_digit > 0:
    message = "negative"
elif last_digit == 0:
    message = "zero"
else:
    message = "positive"

# Print the final message
print(f"The string Last digit of {number} is {last_digit} {message}")

