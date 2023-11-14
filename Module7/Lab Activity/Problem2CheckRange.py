# David Fonseca
# 11/13/2023
# Problem 2 - This is a function which checks whether a number is in a given range. Use
# range(1,10). Print whether the number is in or not in the range.

import math


def is_number_in_range(n):
    # Calculating area
    if n in range(1, 10):
        return True
    else:
        return False


# User input
number = int(input("Enter a number from 1 to 9: "))

# Print the result
if is_number_in_range(number):
    print(f"{number} is in the range")
else:
    print(f"{number} is not in the range")
