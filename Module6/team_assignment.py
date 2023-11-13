# David Fonseca
# 11/11/2023
# This program takes a number (input) from the user and guess a randomly
# generated number. Provide the user with an opportunity to guess higher
# or lower, depending on the randomly generated number.

import random

# Randomly generated number
random_number = random.randrange(1, 11)


while True:

    # User input - integer
    guess = int(input("Please guess number between 1 and 10: "))

    # Evaluate guess
    if guess == random_number:
        print("Well done, you guessed it")
        break
    elif guess < random_number:
        print("Please guess higher")
    elif guess > random_number:
        print("Please guess lower")

    # Check if user would like to guess again
    try_again = input("Would you like to guess another number (Y/N)? ")
    if try_again.lower() == "n":
        break
    else:
        continue
