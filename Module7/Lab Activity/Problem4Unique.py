# David Fonseca
# 11/13/2023
# Problem 4 - This is a function which makes a list of numbers and returns a new list with
# unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append
# function.

import math

numbers = [1, 3, 3, 3, 6, 2, 3, 5]


def unique_elements(numbers_list):
    unique = []
    for i in numbers_list:
        if i not in unique:
            unique.append(i)
    return unique


# Print filtered list
print(unique_elements(numbers))
