# Main menu. Function that starts or quits the game.
import global_variables as gv
import chapters as c
import time


def intro():
    # Game Introduction
    print("\nAs a seasoned investigator known for your sharp instincts"
          "\nand relentless pursuit of justice, recently transferred to"
          "\nthe quiet town of Raven's Hollow, you're about to face a "
          "\ncase that will challenge your skills and intuition like never before.")

    # Get player's name
    player_name = input("\nLet's start with your name: ")
    # Initialize global variables
    gv.g_variables(player_name)

    # Game objective
    print("\nYour objective is to solve the mysterious murder of Mayor Richard Thornton."
          "\nAs you explore the secrets of Raven's Hollow, you must gather clues,"
          "\ninterrogate suspects, and navigate a web of lies to uncover the truth.")


def start():
    c.one.start()

