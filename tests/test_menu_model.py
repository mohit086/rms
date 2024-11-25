import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import unittest
from models.menu import MenuItem, Menu

class TestMenuModel(unittest.TestCase):

    def test_menu_item_creation(self):
        item = MenuItem(1, 'Pizza', 'Delicious cheese pizza', 9.99, True)
        self.assertEqual(item.item_id, 1)
        self.assertEqual(item.name, 'Pizza')
        self.assertEqual(item.price, 9.99)
        self.assertTrue(item.is_available)

    def test_menu_add_item(self):
        menu = Menu()
        item = MenuItem(1, 'Pizza', 'Delicious cheese pizza', 9.99, True)
        menu.add_item(item)
        self.assertEqual(len(menu.items), 1)
        self.assertEqual(menu.items[0].name, 'Pizza')

    def test_menu_remove_item(self):
        menu = Menu()
        item = MenuItem(1, 'Pizza', 'Delicious cheese pizza', 9.99, True)
        menu.add_item(item)
        menu.remove_item(1)
        self.assertEqual(len(menu.items), 0)

    def test_update_menu_item(self):
        item = MenuItem(1, 'Pizza', 'Delicious cheese pizza', 9.99, True)
        item.update_item(name='Veg Pizza', price=11.99)
        self.assertEqual(item.name, 'Veg Pizza')
        self.assertEqual(item.price, 11.99)

if __name__ == '__main__':
    unittest.main()
