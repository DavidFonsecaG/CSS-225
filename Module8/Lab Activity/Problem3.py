# 11/20/2023
# Problem 3 - Function that takes a list and prints if the value 5 is in that list

def is_five_here(values):
    """Function that checks if 5 is in the list of values"""
    if 5 in values:
        return True
    else:
        return False


if __name__ == "__main__":
    test_values_1 = [3, 5, 6, 7]
    test_values_2 = [3, 6, 7, "five", 5 + 1]
    print(is_five_here(test_values_1))
    print(is_five_here(test_values_2))
