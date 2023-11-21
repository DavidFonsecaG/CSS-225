# 11/20/2023
# Problem 1 - Function that takes two inputs from a user and prints whether they are
# equal or not.

def compare_passwords():
    """Function that compares two passwords"""
    pass_1 = input("Enter your password: ")
    pass_2 = input("Confirm password: ")
    if pass_1 == pass_2:
        return True
    else:
        return False


if __name__ == "__main__":
    if compare_passwords():
        print("Access Granted")
    else:
        print("Access Denied")
