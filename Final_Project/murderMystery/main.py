# Crystal Villa, David Fonseca
# Python game - Murder Mystery
# Project developed for CSS-225 Introduction to Applied Programming

import game
import util as u


def main():
    # Game Intro
    game.intro()

    # Get game data from json file
    data = u.connect_data()

    # Start Game
    game.start(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        begin = input("\nWelcome to Murder Mystery"
                      "\nAs a seasoned investigator known for your sharp instincts, you're "
                      "\nabout to face a case that will challenge your skills and intuition like never before."
                      "\nS to Start: ")

        if begin.lower() == "s":
            main()

        else:
            print("See you next time!")
            exit()
