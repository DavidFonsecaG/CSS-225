class GameState:
    def __init__(self):
        self.chapter = 1
        self.player_location = "Town Square"
        self.crime_scene_investigated = False
        self.witnesses_interviewed = False
        self.mayor_office_examined = False
        self.cryptic_message_deciphered = False

class Chapter:
    def __init__(self, game_state):
        self.game_state = game_state

    def display_options(self):
        raise NotImplementedError("Subclasses must implement display_options")

    def process_choice(self, choice):
        raise NotImplementedError("Subclasses must implement process_choice")

class Chapter1(Chapter):
    def display_options(self):
        print(f"You are currently in the {self.game_state.player_location}")
        print("Options:")
        print("1. Investigate the crime scene.")
        print("2. Interview witnesses.")
        print("3. Examine the mayor's office.")
        print("4. Uncover the meaning behind the cryptic message.")
        print("5. Save and Quit")

    def process_choice(self, player_choice):
        if player_choice == "1":
            self.game_state.crime_scene_investigated = True
            print("You carefully examine the crime scene, finding clues that hint at a larger conspiracy.")
        elif player_choice == "2":
            self.game_state.witnesses_interviewed = True
            print("You talk to the townspeople, uncovering their suspicions and fears about the mayor's activities.")
        elif player_choice == "3":
            self.game_state.mayor_office_examined = True
            print("In the mayor's office, you discover hidden documents suggesting a connection to an underground syndicate.")
        elif player_choice == "4":
            self.game_state.cryptic_message_deciphered = True
            print("Deciphering the cryptic message, you realize it points to a secret meeting location.")
        elif player_choice == "5":
            print("Game saved. Goodbye!")
            return True
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        return False

def main():
    game_state = GameState()
    current_chapter = Chapter1(game_state)

    while True:
        current_chapter.display_options()
        player_choice = input("Enter the number corresponding to your choice: ")

        if current_chapter.process_choice(player_choice):
            break

if __name__ == "__main__":
    main()
