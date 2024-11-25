import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import MagicMock
from services.menu_service import MenuService

class TestMenuService(unittest.TestCase):
    def setUp(self):
        # Create a mock database connection
        self.db_mock = MagicMock()
        self.menu_service = MenuService(self.db_mock)

    def test_get_menu_items(self):
        # Simulate fetching menu items from the database
        self.db_mock.connection.cursor.return_value.fetchall.return_value = [
            {'item_id': 1, 'name': 'Pizza', 'price': 9.99, 'is_available': True},
            {'item_id': 2, 'name': 'Burger', 'price': 5.99, 'is_available': True}
        ]

        items = self.menu_service.get_menu_items()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0]['name'], 'Pizza')

    def test_add_menu_item(self):
        # Simulate adding a menu item
        self.db_mock.connection.cursor.return_value.execute.return_value = None
        self.menu_service.add_menu_item('Pasta', 'Delicious pasta', 7.99, True)
        self.db_mock.connection.cursor.return_value.execute.assert_called_once_with(
            "INSERT INTO menu_items (name, description, price, is_available) VALUES (%s, %s, %s, %s);",
            ('Pasta', 'Delicious pasta', 7.99, True)
        )

    def test_update_menu_item(self):
        # Simulate updating a menu item
        self.db_mock.connection.cursor.return_value.execute.return_value = None
        self.menu_service.update_menu_item(1, 'Pizza', 'Tasty pizza', 10.99, True)
        self.db_mock.connection.cursor.return_value.execute.assert_called_once_with(
            "UPDATE menu_items SET name = %s, description = %s, price = %s, is_available = %s WHERE item_id = %s;",
            ('Pizza', 'Tasty pizza', 10.99, True, 1)
        )

    def test_delete_menu_item(self):
        # Simulate deleting a menu item
        self.db_mock.connection.cursor.return_value.execute.return_value = None
        self.menu_service.delete_menu_item(1)
        self.db_mock.connection.cursor.return_value.execute.assert_called_once_with(
            "DELETE FROM menu_items WHERE item_id = %s;", (1,)
        )

if __name__ == '__main__':
    unittest.main()
