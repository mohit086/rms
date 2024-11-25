class OrderItem:
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity

    def to_dict(self):
        """Return a dictionary representation of the order item."""
        return {
            'item_id': self.item_id,
            'quantity': self.quantity
        }

class Order:
    def __init__(self, order_id, user_id, table_no, order_date):
        self.order_id = order_id
        self.user_id = user_id
        self.table_no = table_no
        self.order_date = order_date
        self.order_items = []  # List of OrderItem objects

    def add_item(self, item_id, quantity):
        """Add an item to the order."""
        self.order_items.append(OrderItem(item_id, quantity))

    def remove_item(self, item_id):
        """Remove an item from the order."""
        self.order_items = [item for item in self.order_items if item.item_id != item_id]

    def to_dict(self):
        """Return a dictionary representation of the order."""
        return {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'table_no': self.table_no,
            'order_date': self.order_date,
            'order_items': [item.to_dict() for item in self.order_items]
        }
