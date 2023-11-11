# David Fonseca
# 11/11/2023
# This program uses a for statement to calculate the factorial of a user input value. Print this value
# as well as the calculated value using the factorial function in the math module.

import math


def calculate_factorial(n):
    # Calculating factorial.
    result = 1
    for x in range(2, n+1):
        result *= x
    return result


# User input - integer
number = int(input("Enter an integer to calculate factorial: "))
# Calculate the factorial
factorial = calculate_factorial(number)

# Print the factorial and the value from math.factorial
print(f"{number}! is equal to: {factorial}")
print(f"Factorial from math module: {math.factorial(number)}")
