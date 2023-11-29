class Detective:

    def __init__(self, name):
        self.name = name
        self.clues = []
        self.tools = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_clues(self):
        return self.clues

    def get_tools(self):
        return self.tools

    def tool_acquired(self, tool):
        return tool in self.tools
