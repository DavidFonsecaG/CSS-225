# David Fonseca
# 10/24/2023
# This program loops a list of numbers and  prints each of the numbers on a new line.
# then it prints each number and its square on a new line.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

for number in numbers:
    print(number)

for number in numbers:
    print(number, "it's square is: {}".format(number**2))


