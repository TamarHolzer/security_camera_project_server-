class User:
    def __init__(self, email, password, id=-1):
        self.id = id
        self.email = email
        self.password = password

    def __str__(self):
        return f"User(ID: {self.id}, Email: {self.email}, Password: {self.password})"
