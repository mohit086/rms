from data_access.db_connection import DatabaseConnection
from data_access.queries import *

class UserService:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def login(self, username, password):
        """Authenticate a user by username and password."""
        cursor = self.db_connection.connection.cursor(dictionary=True)
        cursor.execute(GET_USER_BY_USERNAME, (username,))
        user = cursor.fetchone()
        cursor.close()

        if user and user['password'] == password:  # Compare plain passwords
            return user  # User dictionary
        return None

    def add_employee(self, username, password, name):
        """Add a new employee."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(ADD_USER, (username, password, 'employee', name))  # Store plain password
        self.db_connection.connection.commit()
        cursor.close()

    def get_all_employees(self):
        """Retrieve all employees."""
        cursor = self.db_connection.connection.cursor(dictionary=True)
        cursor.execute(GET_ALL_EMPLOYEES)
        employees = cursor.fetchall()
        cursor.close()
        return employees

    def update_employee(self, user_id, username, password, name):
        """Update an employee's details."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(UPDATE_USER, (username, password, name, user_id))  # Update with plain password
        self.db_connection.connection.commit()
        cursor.close()

    def remove_employee(self, user_id):
        """Remove an employee."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(DELETE_USER, (user_id,))
        self.db_connection.connection.commit()
        cursor.close()
