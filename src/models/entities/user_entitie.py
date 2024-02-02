import datetime

class User:
    def __init__(self, id, name=None, email=None, date=None):
        self.id = id
        self.name = name
        self.email = email
        self.date = datetime.datetime.strftime(date, "%d-%m-%y")
