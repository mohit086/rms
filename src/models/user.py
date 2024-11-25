class User:
    def __init__(self, user_id, username, password, role, name):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role  # 'admin' or 'employee'
        self.name = name

    def to_dict(self):
        """Return a dictionary representation of the user."""
        return {
            'user_id': self.user_id,
            'username': self.username,
            'role': self.role,
            'name': self.name
        }

class Admin(User):
    def __init__(self, user_id, username, password, name):
        super().__init__(user_id, username, password, 'admin', name)

class Employee(User):
    def __init__(self, user_id, username, password, name):
        super().__init__(user_id, username, password, 'employee', name)
