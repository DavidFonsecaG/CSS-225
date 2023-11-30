import json

class GameState:
    def __init__(self):
        self.chapter = 1
        self.player_location = "Town Square"
        self.crime_scene_investigated = False
        self.witnesses_interviewed = False
        self.mayor_office_examined = False
        self.cryptic_message_deciphered = False

game_state = GameState()

def load_game_state():
    try:
        with open("game_state.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return GameState()

def save_game_state():
    with open("game_state.json", "w") as file:
        json.dump(game_state.__dict__, file, indent=4)

def display_options():
    print(f"You are currently in the {game_state.player_location}")
    print("Options:")
    print("1. Investigate the crime scene.")
    print("2. Interview witnesses.")
    print("3. Examine the mayor's office.")
    print("4. Uncover the meaning behind the cryptic message.")
    print("5. Save and Quit")

def investigate_crime_scene():
    game_state.crime_scene_investigated = True
    print("You carefully examine the crime scene, finding clues that hint at a larger conspiracy.")

def interview_witnesses():
    game_state.witnesses_interviewed = True
    print("You talk to the townspeople, uncovering their suspicions and fears about the mayor's activities.")

def examine_mayors_office():
    game_state.mayor_office_examined = True
    print("In the mayor's office, you discover hidden documents suggesting a connection to an underground syndicate.")

def uncover_cryptic_message():
    game_state.cryptic_message_deciphered = True
    print("Deciphering the cryptic message, you realize it points to a secret meeting location.")

def transition_to_chapter_2():
    print("Chapter 2: The Underground Syndicate")
    print("With the information gathered in Chapter 1, you decide to delve deeper into the town's secrets.")
    print("Options:")
    print("1. Meet the informant at the secret location.")
    print("2. Gather more information from the town's residents.")
    print("3. Explore the outskirts of Raven's Hollow for additional clues.")
    print("4. Save and Quit")

def meet_informant():
    print("You meet the informant in the shadows of the abandoned warehouse.")
    print("They reveal critical information about the mayor's involvement with the underground syndicate.")

def gather_information():
    print("You discreetly gather information from the town's residents, learning about hidden dealings and power struggles.")

def explore_outskirts():
    print("Exploring the outskirts, you discover a hidden mansion with potential ties to the syndicate.")
    print("Options:")
    print("1. Infiltrate the mansion.")
    print("2. Confront the mayor directly.")
    print("3. Save and Quit")

def infiltrate_mansion():
    print("You successfully infiltrate the mansion, uncovering more evidence of the syndicate's activities.")

def confront_mayor():
    print("Confronting the mayor, you force them to confess their involvement and expose the syndicate's plans.")

while not (game_state.crime_scene_investigated and game_state.witnesses_interviewed
           and game_state.mayor_office_examined and game_state.cryptic_message_deciphered):
    display_options()
    player_choice = input("Enter the number corresponding to your choice: ")

    if player_choice == "1":
        investigate_crime_scene()
    elif player_choice == "2":
        interview_witnesses()
    elif player_choice == "3":
        examine_mayors_office()
    elif player_choice == "4":
        uncover_cryptic_message()
    elif player_choice == "5":
        save_game_state()
        print("Game saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

save_game_state()

if all([game_state.crime_scene_investigated, game_state.witnesses_interviewed,
        game_state.mayor_office_examined, game_state.cryptic_message_deciphered]):
    transition_to_chapter_2()
    chapter_2_choice = input("Enter the number corresponding to your choice: ")

    if chapter_2_choice == "1":
        meet_informant()
    elif chapter_2_choice == "2":
        gather_information()
    elif chapter_2_choice == "3":
        explore_outskirts()
        outskirts_choice = input("Enter the number corresponding to your choice: ")

        if outskirts_choice == "1":
            infiltrate_mansion()
        elif outskirts_choice == "2":
            confront_mayor()
        elif outskirts_choice == "3":
            save_game_state()
            print("Game saved. Goodbye!")
            "break"
        else:
            print("Invalid choice.")
else:
    print("You cannot proceed to Chapter 2. Please complete all necessary actions.")

    print("You examine the mayor's office for additional information.")
    # Additional logic for examining the mayor's office...

# Function to handle player's choice to uncover the meaning behind the cryptic message
def uncover_cryptic_message():
    game_state.cryptic_message_deciphered = True
    print("You uncover the meaning behind the cryptic message.")
    # Additional logic for deciphering the cryptic message...

# Function to handle the transition to Chapter 2
def transition_to_chapter_2():
    print("Chapter 2: The Underground Syndicate")
    # Additional logic for Chapter 2...

# Main game loop for Chapter 1
while not (game_state.crime_scene_investigated and game_state.witnesses_interviewed
           and game_state.mayor_office_examined and game_state.cryptic_message_deciphered):
    display_options()

    # Get player's choice
    player_choice = input("Enter the number corresponding to your choice: ")

    # Process player's choice
    if player_choice == "1":
        investigate_crime_scene()
    elif player_choice == "2":
        interview_witnesses()
    elif player_choice == "3":
        examine_mayors_office()
    elif player_choice == "4":
        uncover_cryptic_message()
    elif player_choice == "5":
        save_game_state()
        print("Game saved. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

# Save the game state before transitioning to Chapter 2
save_game_state()

# Transition to Chapter 2 if all necessary actions are completed
if all([game_state.crime_scene_investigated, game_state.witnesses_interviewed,
        game_state.mayor_office_examined, game_state.cryptic_message_deciphered]):
    transition_to_chapter_2()
else:
    print("You cannot proceed to Chapter 2. Please complete all necessary actions.")
