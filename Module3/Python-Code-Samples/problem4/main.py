# David Fonseca
# October 14th 2023

# This program computes the area of a circle. Prompt the user to enter
# the radius and print a nice message back to the user with the answer

# Get user input
print("Enter the radius of a circle: ")
radius = int(input("--> "))

# Calculating the area
area = 3.14159 * (radius ** 2)

# Printing the answer
print(f"The area of a circle with a radius of {radius} is {area}.")
