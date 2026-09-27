class User:
    def __init__(self, username):
        self.username = username
        self.roles = set()

    def add_role(self, role):
        self.roles.add(role)