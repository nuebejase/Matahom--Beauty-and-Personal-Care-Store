INSERT INTO user (name, email, password, address, role) VALUES
('Admin User', 'admin@matahom.com', 'admin123', 'Admin Address', 'owner'),
('Customer One', 'customer1@mail.com', 'password123', 'Customer Address', 'customer');


INSERT INTO category (name, description) VALUES
('Skincare', 'Products for skin care'),
('Haircare', 'Hair related products');


INSERT INTO product (category_id, name, description, price, stock, image_url) VALUES
(1, 'Facial Wash', 'Gentle facial wash', 12.99, 100, 'images/facial.jpg'),
(2, 'Hair Shampoo', 'Daily shampoo', 9.99, 200, 'images/shampoo.jpg');


INSERT INTO inventory (product_id, quantity) VALUES
(1, 100),
(2, 200);