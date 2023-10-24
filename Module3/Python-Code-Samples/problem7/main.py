# David Fonseca
# October 14th 2023

# This program asks for the starting day number, and the length of your stay, and
# it will tell you the number of day of the week you will return on.

# Define days of the week
days_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Get user input
print("Enter the starting day number (0-6): ")
starting_day = int(input("--> "))

print("Enter the length of stay (in numbers): ")
nights = int(input("--> "))

# Calculating the number of day of the week you will return on
return_day_number = (starting_day + nights) % 7
return_day = days_week[return_day_number]

# Printing the answer
print(f"You will return on a {return_day} (day {return_day_number}).")
