from data_access.db_connection import DatabaseConnection
from services.user_service import UserService
from services.menu_service import MenuService
from services.order_service import OrderService
from services.bill_service import BillService

def admin_menu(user_service, menu_service, order_service, bill_service):
    """CLI menu for admin users."""
    while True:
        print("\nAdmin Menu:")
        print("1. Manage Menu")
        print("2. Manage Employees")
        print("3. Manage Orders")
        print("4. Manage Bills")
        print("5. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            manage_menu(menu_service)
        elif choice == "2":
            manage_employees(user_service)
        elif choice == "3":
            manage_orders(order_service)
        elif choice == "4":
            manage_bills(bill_service)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def employee_menu(order_service, bill_service):
    """CLI menu for employee users."""
    while True:
        print("\nEmployee Menu:")
        print("1. Create Order")
        print("2. View Order")
        print("3. Generate Bill")
        print("4. Mark Bill as Paid")
        print("5. Logout")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_order(order_service)
        elif choice == "2":
            view_order(order_service)
        elif choice == "3":
            generate_bill(order_service, bill_service)
        elif choice == "4":
            mark_bill_as_paid(bill_service)
        elif choice == "5":
            print("Logging out...")
            break
        else:
            print("Invalid choice, please try again.")

def manage_menu(menu_service):
    """CLI menu for managing the menu."""
    while True:
        print("\nManage Menu:")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Update Menu Item")
        print("4. Remove Menu Item")
        print("5. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            items = menu_service.get_menu_items()
            for item in items:
                print_menu_item(item)
        elif choice == "2":
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: "))
            is_available = input("Is the item available? (yes/no): ").lower() == "yes"
            menu_service.add_menu_item(name, description, price, is_available)
            print("Menu item added successfully!")
        elif choice == "3":
            item_id = int(input("Enter menu item ID to update: "))
            name = input("Enter new name: ")
            description = input("Enter new description: ")
            price = float(input("Enter new price: "))
            is_available = input("Is the item available? (yes/no): ").lower() == "yes"
            menu_service.update_menu_item(item_id, name, description, price, is_available)
            print("Menu item updated successfully!")
        elif choice == "4":
            item_id = int(input("Enter menu item ID to remove: "))
            menu_service.delete_menu_item(item_id)
            print("Menu item removed successfully!")
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def manage_employees(user_service):
    """CLI menu for managing employees."""
    while True:
        print("\nManage Employees:")
        print("1. View Employees")
        print("2. Add Employee")
        print("3. Update Employee")
        print("4. Remove Employee")
        print("5. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            employees = user_service.get_all_employees()
            for emp in employees:
                print_user(emp)
        elif choice == "2":
            username = input("Enter employee username: ")
            password = input("Enter employee password: ")
            name = input("Enter employee name: ")
            user_service.add_employee(username, password, name)
            print("Employee added successfully!")
        elif choice == "3":
            user_id = int(input("Enter employee ID to update: "))
            username = input("Enter new username: ")
            password = input("Enter new password: ")
            name = input("Enter new name: ")
            user_service.update_employee(user_id, username, password, name)
            print("Employee updated successfully!")
        elif choice == "4":
            user_id = int(input("Enter employee ID to remove: "))
            user_service.remove_employee(user_id)
            print("Employee removed successfully!")
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def manage_orders(order_service):
    """CLI menu for managing orders."""
    while True:
        print("\nManage Orders:")
        print("1. Create Order")
        print("2. View Order")
        print("3. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            create_order(order_service)
        elif choice == "2":
            view_order(order_service)
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def create_order(order_service):
    """Create a new order."""
    user_id = int(input("Enter employee ID: "))
    table_no = int(input("Enter table number: "))
    order_id = order_service.create_order(user_id, table_no)
    print(f"Order created with ID {order_id}.")

    while True:
        item_id = int(input("Enter item ID to add to order (or 0 to finish): "))
        if item_id == 0:
            break
        quantity = int(input("Enter quantity: "))
        order_service.add_order_item(order_id, item_id, quantity)
        print(f"Added item {item_id} to order {order_id}.")

def view_order(order_service):
    """View an existing order."""
    order_id = int(input("Enter order ID to view: "))
    order = order_service.get_order_by_id(order_id)
    print_order(order)

def manage_bills(bill_service):
    """CLI menu for managing bills."""
    while True:
        print("\nManage Bills:")
        print("1. View Bill")
        print("2. Generate Bill")
        print("3. Mark Bill as Paid")
        print("4. Back to Admin Menu")

        choice = input("Enter your choice: ")
        if choice == "1":
            view_bill(bill_service)
        elif choice == "2":
            generate_bill(bill_service)
        elif choice == "3":
            mark_bill_as_paid(bill_service)
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

def view_bill(bill_service):
    """View an existing bill."""
    bill_id = int(input("Enter bill ID to view: "))
    bill = bill_service.get_bill_details(bill_id)
    print_bill(bill)

def generate_bill(bill_service):
    """Generate a bill for an order."""
    order_id = int(input("Enter order ID to generate bill for: "))
    total_amount = float(input("Enter total amount: "))
    bill_id = bill_service.generate_bill(order_id, total_amount)
    print(f"Bill generated with ID {bill_id}.")

def mark_bill_as_paid(bill_service):
    """Mark a bill as paid."""
    bill_id = int(input("Enter bill ID to mark as paid: "))
    bill_service.mark_bill_as_paid(bill_id)
    print(f"Bill {bill_id} marked as paid.")

# Helper functions for pretty printing
def print_menu_item(item):
    """Formatted printing of a menu item."""
    print(f"Item ID: {item['item_id']}, Name: {item['name']}, Price: {item['price']}, Available: {'Yes' if item['is_available'] else 'No'}")

def print_user(user):
    """Formatted printing of a user (employee)."""
    print(f"User ID: {user['user_id']}, Username: {user['username']}, Name: {user['name']}, Role: {user['role']}")

def print_order(order):
    """Formatted printing of an order."""
    print(f"Order ID: {order['order_id']}, Table No: {order['table_no']}, Order Date: {order['order_date']}")
    print("Items:")
    for item in order['items']:
        print(f"  Item ID: {item['item_id']}, Quantity: {item['quantity']}")

def print_bill(bill):
    """Formatted printing of a bill."""
    if bill:
        print(f"Bill ID: {bill['bill_id']}, Order ID: {bill['order_id']}, Total Amount: {bill['total_amount']}, Payment Status: {bill['payment_status']}")
    else:
        print("No bill found.")
        
# Entry point
if __name__ == "__main__":
    # Initialize the database connection
    db = DatabaseConnection(host="localhost", user="root", password="admin", database="restaurant")
    db.connect()

    # Initialize services
    user_service = UserService(db)
    menu_service = MenuService(db)
    order_service = OrderService(db)
    bill_service = BillService(db)

    # CLI starts here
    print("Welcome to the Restaurant Management System!")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = user_service.login(username, password)

    if user:
        print(f"Welcome, {user['name']}!")
        if user['role'] == "admin":
            admin_menu(user_service, menu_service, order_service, bill_service)
        elif user['role'] == "employee":
            employee_menu(order_service, bill_service)
        else:
            print("Unknown role. Exiting.")
    else:
        print("Authentication failed. Exiting.")

    # Close the database connection
    db.close()