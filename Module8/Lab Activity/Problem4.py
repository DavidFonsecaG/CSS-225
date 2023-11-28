# 11/20/2023
# Problem 4 - Function that takes a year as a parameter and returns True if the year is a
# leap year, False if it is otherwise

def leap_year(year):
    """Function that checks if a year is leap or not"""
    if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print(leap_year(2000))
    print(leap_year(1700))
    print(leap_year(500))
