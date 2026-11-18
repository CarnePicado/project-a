class Task:
    def __init__(self, title, description=""):
        self.title = title
        self.description = description
        self.completed = False

    def update_description(self, description):
        self.description = description

    def complete(self):
        self.completed = True
