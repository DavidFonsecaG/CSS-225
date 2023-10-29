# David Fonseca
# 10/24/2023
# This program  iterates the integers from 1 to 50. For multiples of three
# print “Divisible by three” instead of the number and for the multiples of five print “Divisible by
# five”. For numbers which are multiples of both three and five print “Divisible by both”.

for i in range(1,51):
    if i%15 == 0:
        print("Divisible by both")
    elif i%5 == 0:
        print("Divisible by five")
    elif i%3 == 0:
        print("Divisible by three")
    else:
        print(i)