import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from models.order import OrderItem, Order

class TestOrderModel(unittest.TestCase):

    def test_order_item_creation(self):
        order_item = OrderItem(1, 2)
        self.assertEqual(order_item.item_id, 1)
        self.assertEqual(order_item.quantity, 2)

    def test_order_creation(self):
        order = Order(1, 1, 5, '2024-11-25')
        self.assertEqual(order.order_id, 1)
        self.assertEqual(order.table_no, 5)
        self.assertEqual(order.order_date, '2024-11-25')

    def test_add_order_item(self):
        order = Order(1, 1, 5, '2024-11-25')
        order.add_item(1, 2)
        self.assertEqual(len(order.order_items), 1)
        self.assertEqual(order.order_items[0].item_id, 1)

    def test_remove_order_item(self):
        order = Order(1, 1, 5, '2024-11-25')
        order.add_item(1, 2)
        order.remove_item(1)
        self.assertEqual(len(order.order_items), 0)

    def test_order_to_dict(self):
        order = Order(1, 1, 5, '2024-11-25')
        order.add_item(1, 2)
        order_dict = order.to_dict()
        self.assertEqual(order_dict['order_id'], 1)
        self.assertEqual(len(order_dict['order_items']), 1)

if __name__ == '__main__':
    unittest.main()
