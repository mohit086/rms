import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import MagicMock
from services.user_service import UserService

class TestUserService(unittest.TestCase):
    def setUp(self):
        # Create a mock database connection
        self.db_mock = MagicMock()
        self.user_service = UserService(self.db_mock)

    def test_login_success(self):
        # Simulate the response from the database for a successful login
        self.db_mock.connection.cursor.return_value.fetchone.return_value = {
            'user_id': 1, 'username': 'testuser', 'password': 'password', 'role': 'admin', 'name': 'Test User'
        }

        user = self.user_service.login('testuser', 'password')
        self.assertIsNotNone(user)
        self.assertEqual(user['username'], 'testuser')

    def test_login_failure(self):
        # Simulate the response from the database for a failed login
        self.db_mock.connection.cursor.return_value.fetchone.return_value = None

        user = self.user_service.login('wronguser', 'wrongpassword')
        self.assertIsNone(user)

    def test_add_employee(self):
        # Simulate adding an employee
        self.db_mock.connection.cursor.return_value.execute.return_value = None
        self.user_service.add_employee('newuser', 'password', 'New User')
        self.db_mock.connection.cursor.return_value.execute.assert_called_once_with(
            "INSERT INTO users (username, password, role, name) VALUES (%s, %s, %s, %s);",
            ('newuser', 'password', 'employee', 'New User')
        )

    def test_remove_employee(self):
        # Simulate removing an employee
        self.db_mock.connection.cursor.return_value.execute.return_value = None
        self.user_service.remove_employee(1)
        self.db_mock.connection.cursor.return_value.execute.assert_called_once_with(
            "DELETE FROM users WHERE user_id = %s;", (1,)
        )

if __name__ == '__main__':
    unittest.main()
