import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from unittest.mock import MagicMock
from services.order_service import OrderService

class TestOrderService(unittest.TestCase):
    def setUp(self):
        # Create a mock database connection
        self.db_mock = MagicMock()
        self.order_service = OrderService(self.db_mock)

    def test_create_order(self):
        # Simulate creating an order
        self.db_mock.connection.cursor.return_value.lastrowid = 1
        order_id = self.order_service.create_order(1, 5)
        self.assertEqual(order_id, 1)

    def test_add_order_item(self):
        # Simulate adding an item to an order
        self.db_mock.connection.cursor.return_value.execute.return_value = None
        self.order_service.add_order_item(1, 1, 2)
        self.db_mock.connection.cursor.return_value.execute.assert_called_once_with(
            "INSERT INTO order_items (order_id, item_id, quantity) VALUES (%s, %s, %s);",
            (1, 1, 2)
        )

    def test_get_order_by_id(self):
        # Simulate fetching an order by ID
        self.db_mock.connection.cursor.return_value.fetchone.return_value = {'order_id': 1, 'table_no': 5, 'order_date': '2024-11-25'}
        self.db_mock.connection.cursor.return_value.fetchall.return_value = [{'item_id': 1, 'quantity': 2}]
        
        order = self.order_service.get_order_by_id(1)
        self.assertEqual(order['order_id'], 1)
        self.assertEqual(len(order['items']), 1)

if __name__ == '__main__':
    unittest.main()
