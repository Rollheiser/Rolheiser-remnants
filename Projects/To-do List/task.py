""" This is the class necessary for the "to-do list", here it contains its attributes
    such as title, description, date, priority, status, etc. """

class Task:
    def __init__(self, title: str, description: str, date: str, priority_level: str, status: bool):
        self.title = title
        self.description = description
        self.date = date
        self.priority_level = priority_level
        self.status = status
    
    def return_task_status(self):
        if not self.status:
            return "Pending"
        
        return "Completed"
