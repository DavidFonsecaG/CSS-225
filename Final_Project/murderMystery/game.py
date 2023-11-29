# Main menu. Function that starts or quits the game.
import global_variables as gv
import chapters.one as c_one
import time


def intro():
    # Get player's name
    player_name = input("Let's start with your name: ")
    # Initialize global variables
    gv.g_variables(player_name)

    # Game objective
    print(f"\n{player_name}, your objective is to solve the mysterious murder of Mayor Richard Thornton."
          "\nAs you explore the secrets of Raven's Hollow, you must gather clues,"
          "\ninterrogate suspects, and navigate a web of lies to uncover the truth.")
    time.sleep(2)


def start(data):
    c_one.start(data["chapters"]["1"])

