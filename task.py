import datetime
class Task:
    id = 1
    def __init__(self, name):
        self.name = name
        self.id = Task.id
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        Task.id += 1