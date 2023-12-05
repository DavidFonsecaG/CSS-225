class Detective:

    def __init__(self ):
        self.clues = []
        self.weapons = ['notebook']


    def get_clues(self):
        return self.clues

    def get_weapons(self):
        return self.weapons

    def set_clues(self, clue):
        self.clues.append(clue)

    def set_weapons(self, weapon):
        self.weapons.append(weapon)

    def profile(self):
        return self.clues, self.weapons

