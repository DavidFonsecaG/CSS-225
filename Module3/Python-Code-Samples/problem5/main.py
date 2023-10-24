# David Fonseca
# October 14th 2023

# This program computes MPG for a car. Prompt the user to enter the
# number of miles driven and the number of gallons used. Print a nice message with the answer.

# Get user input
print("Enter the number of miles driven: ")
miles = int(input("--> "))

print("Enter the number of gallons used: ")
gallons = int(input("--> "))

# Calculating the MPG
mpg = miles / gallons

# Printing the answer
print(f"The MPG for this car is {mpg}")
