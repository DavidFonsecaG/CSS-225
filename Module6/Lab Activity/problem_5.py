# David Fonseca
# 11/11/2023
# This program computes the conversion of radiant to degrees given a user input value.
# Print this value as well as the calculated value
# using the degrees function in the math module.

import math


def convert_radians(r):
    # Conversion based on 360 degrees is equal to
    # 2pi radians. 1 radian equals 180/pi degrees.
    result = r * (180 / math.pi)

    return result


# User input - Radians
radians = int(input("Enter radians to be converted to degrees (Number): "))
# Calculate the conversion
degrees = convert_radians(radians)

# Print the conversion and the value from math.degrees
print(f"{radians} radians are {degrees} degrees")
print(f"Radians from math module: {math.degrees(radians)}")
