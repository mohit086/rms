from data_access.queries import *

class OrderService:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create_order(self, user_id, table_no):
        """Create a new order."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(CREATE_ORDER, (user_id, table_no))
        order_id = cursor.lastrowid
        self.db_connection.connection.commit()
        cursor.close()
        return order_id

    def add_order_item(self, order_id, item_id, quantity):
        """Add an item to an order."""
        cursor = self.db_connection.connection.cursor()
        cursor.execute(ADD_ORDER_ITEM, (order_id, item_id, quantity))
        self.db_connection.connection.commit()
        cursor.close()

    def get_order_by_id(self, order_id):
        """Retrieve an order by ID."""
        cursor = self.db_connection.connection.cursor(dictionary=True)
        cursor.execute(GET_ORDER_BY_ID, (order_id,))
        order = cursor.fetchone()
        cursor.execute(GET_ORDER_ITEMS, (order_id,))
        order['items'] = cursor.fetchall()
        cursor.close()
        return order
