import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from models.user import User, Admin, Employee

class TestUserModel(unittest.TestCase):

    def test_user_creation(self):
        # Test that a user can be created
        user = User(1, 'testuser', 'password', 'admin', 'Test User')
        self.assertEqual(user.user_id, 1)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.role, 'admin')
        self.assertEqual(user.name, 'Test User')

    def test_admin_creation(self):
        # Test that an admin can be created
        admin = Admin(1, 'adminuser', 'password', 'Admin User')
        self.assertIsInstance(admin, Admin)
        self.assertEqual(admin.role, 'admin')

    def test_employee_creation(self):
        # Test that an employee can be created
        employee = Employee(2, 'employeeuser', 'password', 'Employee User')
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.role, 'employee')

if __name__ == '__main__':
    unittest.main()
