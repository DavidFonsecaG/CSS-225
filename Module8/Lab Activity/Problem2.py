# 11/20/2023
# Problem 2 - Function that takes two inputs from a user and prints whether the sum is
# greater than 10, less than 10, or equal to 10.

def compare_numbers(num_1, num_2):
    """Function that checks if the sum of two integers is greater, less, or equal to 10"""
    total = num_1 + num_2

    if total > 10:
        return f"{total} is greater than 10"
    elif total < 10:
        return f"{total} is less than 10"
    else:
        return f"{total} is equal to 10"


if __name__ == "__main__":
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter second number: "))
    print(compare_numbers(number_1, number_2))
