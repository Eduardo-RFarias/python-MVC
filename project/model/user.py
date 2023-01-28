class User:
    def __init__(self, username, email, password, id=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __str__(self):
        return f"User[username={self.username}, email={self.email}]"

    def __eq__(self, __o: object) -> bool:
        return self.id == __o.id
