# David Fonseca
# 11/28/2023
# Problem 3 - while loop, ask the user to enter a number. Append each entered number
# to a list and add them together. Continue asking for a number until the sum of the list of
# numbers is greater than 100.

numbers = []
sum = 0

while sum <= 100:
    num = int(input("Enter a  number: "))

    numbers.append(num)

    sum += num

print(f"The sum of the numbers is {sum}")
print(f"Here is the list of numbers:\n{numbers}")

