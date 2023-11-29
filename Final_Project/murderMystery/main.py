# Crystal Villa, David Fonseca
# Python game - Murder Mystery
# Project developed for CSS-225 Introduction to Applied Programming

import game


def main():
    # Game Intro
    game.intro()

    # Start Game
    game.start()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        begin = input("\nWelcome to Murder Mystery"
                      "\nS to Start: ")

        if begin.lower() == "s":
            main()

        else:
            print("See you next time!")
            exit()
