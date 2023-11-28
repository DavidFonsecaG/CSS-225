# David Fonseca
# 11/28/2023
# Problem 1 - infinite loop that prints “Infinite”. An infinite loop never ends. The
# condition is always true.

n = 10
answer = 1
while n < 15:
                    answer = answer + n
                    n = n + 1
print(answer)

