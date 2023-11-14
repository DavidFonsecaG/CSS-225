# David Fonseca
# 11/13/2023
# Problem 3 - This is a function which multiplies all
# the numbers in a list. Use list [5, 2, 7, -1]

import math

numbers = [5, 2, 7, -1]


def multiply_numbers(numbers_list):
    total = 1
    for n in numbers_list:
        total *= n
    return total


def print_list(numbers_list):
    return ' x '.join(map(str, numbers_list))


# Calculate the multiplication
result = multiply_numbers(numbers)

# Print the result
print(f"{print_list(numbers)} is equal to: {result} ")
