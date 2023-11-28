# David Fonseca
# 11/28/2023
# Problem 2 - while loop, create a list called L that contains the numbers 0 to 10. On each
# iteration, the loop should append the current value of a counter variable to the list and then
# increase the counter by 1. The while loop should stop once the counter variable is greater than
# 10.

l = []
counter = 0

while counter <= 10:
    l.append(counter)
    counter += 1


print(l)
