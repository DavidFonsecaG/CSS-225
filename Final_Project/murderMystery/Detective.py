class Detective:

    def __init__(self, name, town, description, objective):
        self.name = name
        self.clues = []
        self.tools = []
        self.town = town
        self.description = description
        self.objective = objective

    def get_name(self):
        return self.name

    def get_town(self):
        return self.town

    def get_objective(self):
        return self.objective

    def get_clues(self):
        return self.clues

    def get_tools(self):
        return self.tools

    def tool_acquired(self, tool):
        return tool in self.tools

    def chose_action(self):
        return input("--> ")

    def introduce_self(self):
        return "\nYou are detective " + self.name + self.description
