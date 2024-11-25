class MenuItem:
    def __init__(self, item_id, name, description, price, is_available=True):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
        self.is_available = is_available

    def update_item(self, name=None, description=None, price=None, is_available=None):
        """Update the menu item details."""
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if price is not None:
            self.price = price
        if is_available is not None:
            self.is_available = is_available

    def to_dict(self):
        """Return a dictionary representation of the menu item."""
        return {
            'item_id': self.item_id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'is_available': self.is_available
        }

class Menu:
    def __init__(self):
        self.items = []  # List of MenuItem objects

    def add_item(self, menu_item):
        """Add a menu item."""
        self.items.append(menu_item)

    def remove_item(self, item_id):
        """Remove a menu item."""
        self.items = [item for item in self.items if item.item_id != item_id]

    def get_item(self, item_id):
        """Retrieve a menu item by ID."""
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def to_list(self):
        """Return a list of dictionary representations of the menu."""
        return [item.to_dict() for item in self.items]
