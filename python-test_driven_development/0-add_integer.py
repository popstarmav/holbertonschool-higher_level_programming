def add_integer(a, b=98):
    # Check if a and b are integers or can be turned into integers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")

    # Convert a and b to integers if they are floats
    a = int(a)
    b = int(b)

    # Add the two integers
    result = a + b

    # Return the result
    return result
