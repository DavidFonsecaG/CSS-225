# David Fonseca
# 11/11/2023
# This program uses random.choice to select a day of the week from a list and print that day.

import random

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

day = random.choice(days)
print(f"The day chosen is: {day}")
