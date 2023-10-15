class Task():
    def __init__(self,description,due_date,date_created,status = 'pending') -> None:
        self.description = description
        self.due_date = due_date
        self.date_created = date_created
        self.status = status
        self.date_updated = date_created