# 11/20/2023
# Problem 5 - Character class. Adding Function that checks whether your game character
# has picked up all the items needed to perform certain tasks and checks against any
# status debuffs. Confirm checks with print statements.

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

    def can_perform_task(self, task):
        # Defining the requirements and restrictions for each task
        task_requirements = {
            'Climb a mountain': {
                'needed_items': ['rope', 'coat', 'first aid kit'],
                'forbidden_debuffs': ['slow']
            },
            'Cook a meal': {
                'needed_items': ['pan', 'groceries'],
                'forbidden_debuffs': ['small']
            },
            'Write a book': {
                'needed_items': ['pen', 'paper', 'idea'],
                'forbidden_debuffs': ['confusion']
            }
        }

        # Getting the requirements for the specified task
        requirements = task_requirements.get(task)

        # Checking if the character has all required items
        if not all(item in self.weapons for item in requirements['needed_items']):
            print(f"Cannot perform {task}: Missing required items.")
            return False

        # Checking if the character has any forbidden debuffs
        if any(debuff in self.weaknesses for debuff in requirements['forbidden_debuffs']):
            print(f"Cannot perform {task}: Forbidden debuff present.")
            return False

        # If all checks pass
        print(f"Can perform {task}!")
        return True


if __name__ == "__main__":
    player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

    # Check tasks
    player1.can_perform_task('Climb a mountain')
    player1.can_perform_task('Cook a meal')
    player1.can_perform_task('Write a book')
