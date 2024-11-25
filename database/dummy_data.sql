-- Populate Users
INSERT INTO users (username, password, role, name) VALUES
('admin1', 'admin123', 'admin', 'Admin One'),
('employee1', 'employee123', 'employee', 'Employee One'),
('employee2', 'employee456', 'employee', 'Employee Two');

-- Populate Menu Items
INSERT INTO menu_items (name, description, price, is_available) VALUES
('Margherita Pizza', 'Classic cheese pizza with fresh tomato sauce.', 9.99, TRUE),
('Pepperoni Pizza', 'Spicy pepperoni on mozzarella cheese.', 12.99, TRUE),
('Caesar Salad', 'Fresh romaine lettuce with Caesar dressing.', 7.99, TRUE),
('Grilled Chicken Sandwich', 'Grilled chicken with lettuce and tomato.', 8.99, TRUE),
('Chocolate Cake', 'Rich chocolate cake with layers of ganache.', 5.99, TRUE);

-- Populate Orders
INSERT INTO orders (user_id, table_no) VALUES
(2, 5),
(3, 3),
(2, 7);

-- Populate Order Items
INSERT INTO order_items (order_id, item_id, quantity) VALUES
(1, 1, 2),
(1, 3, 1),
(2, 2, 1),
(2, 5, 2),
(3, 4, 1);

-- Populate Bills
INSERT INTO bills (order_id, total_amount, payment_status) VALUES
(1, 27.97, 'paid'),
(2, 24.97, 'unpaid'),
(3, 8.99, 'unpaid');
