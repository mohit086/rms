# User Queries
GET_USER_BY_USERNAME = "SELECT * FROM users WHERE username = %s;"
ADD_USER = "INSERT INTO users (username, password, role, name) VALUES (%s, %s, %s, %s);"
GET_ALL_EMPLOYEES = "SELECT * FROM users WHERE role = 'employee';"
UPDATE_USER = "UPDATE users SET username = %s, password = %s, name = %s WHERE user_id = %s;"
DELETE_USER = "DELETE FROM users WHERE user_id = %s;"

# Menu Queries
GET_ALL_MENU_ITEMS = "SELECT * FROM menu_items;"
GET_MENU_ITEM_BY_ID = "SELECT * FROM menu_items WHERE item_id = %s;"
ADD_MENU_ITEM = "INSERT INTO menu_items (name, description, price, is_available) VALUES (%s, %s, %s, %s);"
UPDATE_MENU_ITEM = "UPDATE menu_items SET name = %s, description = %s, price = %s, is_available = %s WHERE item_id = %s;"
DELETE_MENU_ITEM = "DELETE FROM menu_items WHERE item_id = %s;"

# Order Queries
CREATE_ORDER = "INSERT INTO orders (user_id, table_no) VALUES (%s, %s);"
GET_ORDER_BY_ID = "SELECT * FROM orders WHERE order_id = %s;"
ADD_ORDER_ITEM = "INSERT INTO order_items (order_id, item_id, quantity) VALUES (%s, %s, %s);"
GET_ORDER_ITEMS = "SELECT * FROM order_items WHERE order_id = %s;"

# Bill Queries
CREATE_BILL = "INSERT INTO bills (order_id, total_amount, payment_status) VALUES (%s, %s, 'unpaid');"
GET_BILL_BY_ID = "SELECT * FROM bills WHERE bill_id = %s;"
UPDATE_BILL_STATUS = "UPDATE bills SET payment_status = 'paid' WHERE bill_id = %s;"
