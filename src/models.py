class Task:
    def __init__(self, title, description="", due_date=""):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def update_description(self, description):
        self.description = description

    def complete(self):
        self.completed = True
