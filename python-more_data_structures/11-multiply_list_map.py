def multiply_list_map(my_list=[], number=0):
    # Using map with a lambda function to multiply each element by the number
    result = list(map(lambda x: x * number, my_list))
    return result
