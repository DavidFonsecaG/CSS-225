# David Fonseca
# October 14th 2023

# This program asks the user for their name and greets them with their
# name only for the users you and your instructor

# Get user input
role = int(input("1. Student \n2. Instructor \n3. Other \nEnter your role (Numbers only 1-3): \n--> "))

# Print greeting base on role
if (role == 1 or 2):
    username = input("Enter your name: ")
    print("Hello", username)
else:
    print("Hello there!")
