# David Fonseca
# 11/11/2023
# This program computes the an approximation for pi and then
# print that value as well as the value of math.pi from the math module.

import math


def approximate_pi():
    # Using Leibniz formula for approximating pi
    # summing the first 1000 terms
    pi_approx = 0
    for k in range(1000):
        pi_approx += ((-1) ** k) / (2 * k + 1)
    pi_approx *= 4

    return pi_approx


# Calculate the approximation
pi_approximation = approximate_pi()

# Print the approximation and the value from math.pi
print(f"Approximated value of pi: {pi_approximation}")
print(f"Value of pi from math module: {math.pi}")
