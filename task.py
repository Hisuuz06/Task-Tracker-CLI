import datetime
class Task:
    def __init__(self, name):
        self.name = name
        self.id = None
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    @classmethod
    def from_dict(cls, data):
        task = cls(data['name'])
        task.created_at = datetime.datetime.strptime(data['created_at'], "%H:%M:%S %d/%m/%Y")
        task.updated_at = datetime.datetime.strptime(data['updated_at'], "%H:%M:%S %d/%m/%Y")
        return task

    def to_dict(self):
        return {
            'name': self.name,
            'created_at': self.created_at.strftime("%H:%M:%S %d/%m/%Y"),
            'updated_at': self.updated_at.strftime("%H:%M:%S %d/%m/%Y"),
        }
    
    def update_name(self, new_name):
        self.name = new_name
        self.updated_at = datetime.datetime.now()