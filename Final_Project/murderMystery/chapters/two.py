# your_module_name.py

class GameState:
    def __init__(self):
        self.chapter = 1
        self.player_location = "Town Square"
        self.crime_scene_investigated = False
        self.witnesses_interviewed = False
        self.mayor_office_examined = False
        self.cryptic_message_deciphered = False
        self.informant_met = False
        self.town_residents_gathered_info = False
        self.outskirts_explored = False
        self.mansion_infiltrated = False
        self.mayor_confronted = False

def save_game_state(game_state):
    # Implement your own save logic here if needed
    with open("game_state.txt", "w") as file:
        file.write(f"{game_state.__dict__}")

def load_game_state():
    # Implement your own load logic here if needed
    game_state = GameState()
    try:
        with open("game_state.txt", "r") as file:
            data = eval(file.read())
            game_state.__dict__.update(data)
    except FileNotFoundError:
        pass
    return game_state

class Chapter:
    def __init__(self, game_state):
        self.game_state = game_state

    def display_options(self):
        raise NotImplementedError("Subclasses must implement display_options")

    def process_choice(self, choice):
        raise NotImplementedError("Subclasses must implement process_choice")

class Chapter2(Chapter):
    def display_options(self):
        print("Chapter 2: The Underground Syndicate")
        print("With the information gathered in Chapter 1, you decide to delve deeper into the town's secrets.")
        print("Options:")
        print("1. Meet the informant at the secret location.")
        print("2. Gather more information from the town's residents.")
        print("3. Explore the outskirts of Raven's Hollow for additional clues.")
        print("4. Save and Quit")

    def process_choice(self, chapter_2_choice):
        if chapter_2_choice == "1":
            self.game_state.informant_met = True
            print("You meet the informant in the shadows of the abandoned warehouse.")
            print("They reveal critical information about the mayor's involvement with the underground syndicate.")
        elif chapter_2_choice == "2":
            self.game_state.town_residents_gathered_info = True
            print("You discreetly gather information from the town's residents, learning about hidden dealings and power struggles.")
        elif chapter_2_choice == "3":
            self.game_state.outskirts_explored = True
            print("Exploring the outskirts, you discover a hidden mansion with potential ties to the syndicate.")
            print("Options:")
            print("1. Infiltrate the mansion.")
            print("2. Confront the mayor directly.")
            print("3. Save and Quit")
        elif chapter_2_choice == "4":
            save_game_state(self.game_state)
            print("Game saved. Goodbye!")
            return True
        else:
            print("Invalid choice.")
        return False

    def process_outskirts_choice(self, outskirts_choice):
        if outskirts_choice == "1":
            self.game_state.mansion_infiltrated = True
            print("You successfully infiltrate the mansion, uncovering more evidence of the syndicate's activities.")
        elif outskirts_choice == "2":
            self.game_state.mayor_confronted = True
            print("Confronting the mayor, you force them to confess their involvement and expose the syndicate's plans.")
        elif outskirts_choice == "3":
            save_game_state(self.game_state)
            print("Game saved. Goodbye!")
            return True
        else:
            print("Invalid choice.")
        return False

def main():
    game_state = load_game_state()
    current_chapter = Chapter2(game_state)

    while True:
        current_chapter.display_options()
        chapter_2_choice = input("Enter the number corresponding to your choice: ")

        if current_chapter.process_choice(chapter_2_choice):
            break

        if current_chapter.game_state.player_location == "Outskirts":
            outskirts_choice = input("Enter the number corresponding to your choice: ")
            if current_chapter.process_outskirts_choice(outskirts_choice):
                break

if __name__ == "__main__":
    main()

