from data_access.queries import *

class MenuService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_menu_items(self):
        """Retrieve all menu items."""
        cursor = self.db_connection.connection.cursor(dictionary=True)
        cursor.execute(GET_ALL_MENU_ITEMS)
        items = cursor.fetchall()
        cursor.close()
        return items

    def add_menu_item(self, name, description, price, is_available=True):
        """Add a new menu item."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(ADD_MENU_ITEM, (name, description, price, is_available))
        self.db_connection.connection.commit()
        cursor.close()

    def update_menu_item(self, item_id, name, description, price, is_available):
        """Update menu item details."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(UPDATE_MENU_ITEM, (name, description, price, is_available, item_id))
        self.db_connection.connection.commit()
        cursor.close()

    def delete_menu_item(self, item_id):
        """Delete a menu item."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(DELETE_MENU_ITEM, (item_id,))
        self.db_connection.connection.commit()
        cursor.close()
