class Task:
    def __init__(self, title, description="", priority="Средний"):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False

    def complete(self):
        self.completed = True
