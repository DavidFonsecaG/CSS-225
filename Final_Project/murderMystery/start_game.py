# Main menu. Function that starts or quits the game.
import time
import global_variables as g_var
import chapters.chapter as c


def start_game():
    print(g_var.detective.introduce_self())
    time.sleep(3)

    print(g_var.detective.get_objective())
    time.sleep(3)

    c.start_chapters()



def menu():
    run = True
    while run:
        begin = input("\n===================Murder Mystery====================="
                      "\nEnter B to begin, or Q to quit:"
                      "\n--> ")

        if begin.lower() == "b":
            start_game()

        else:
            print("See you next time.")
            run = False

    return exit()
