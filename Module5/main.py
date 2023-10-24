# Denife the variable 'answer'
answer  = 42 # You can replace this with any int value

guess = int(input("Enter a number: "))

# Check if the guess is equal to the answer
if guess == answer:
    print("You got it first time")
else:
    # Provide feedback based on guess
    if guess < answer:
        print("Please guess higher")
    else:
        print("PLease guess lower")

# Check if the new guess is correct
if guess == answer:
    print("Well done, you guessed it")
else:
    print("Sorry, you have not guessed correctly")

