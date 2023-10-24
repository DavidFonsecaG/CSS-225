# David Fonseca
# This programs prints a number of options presented to the
# user and allows the user to select an option from the list.

options = ["Learn Python", "Learn Java", "Go Swimming", "Have Dinner", "Go to bed"]

while True:
    # Printing optios
    print("="*46)
    print("Please choose your option from the list below: \n")
    for index, option in enumerate(options):
        print("{0}.".format(index+1), option)
    print("0. Exit \n")

    # Getting input from user
    user_input = input("--> ")
    try:
        user_input_int = int(user_input)
        # Handle user input
        if user_input_int == 0:
            break
        elif 0 < user_input_int <= len(options):
            print("--> You have selected: {} \n".format(options[user_input_int-1]))
        else:
            print("--> {0} is not on the list, try again. \n".format(user_input_int))
    except:
        print("--> {} is not valid value, try again. \n".format(user_input))
