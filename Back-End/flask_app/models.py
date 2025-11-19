from config import db
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    address = db.Column(db.String(255))
    role = db.Column(db.Enum('owner', 'customer'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    orders = db.relationship("Order", backref="user")


class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    products = db.relationship("Product", backref="category")


class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"))
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    price = db.Column(db.Numeric(10,2))
    stock = db.Column(db.Integer)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    inventory = db.relationship("Inventory", uselist=False, backref="product")
    order_items = db.relationship("OrderItems", backref="product")


class Inventory(db.Model):
    inventory_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"))
    quantity = db.Column(db.Integer)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    total_amount = db.Column(db.Numeric(10,2))
    status = db.Column(db.Enum('pending', 'shipped', 'delivered', 'cancelled'), default='pending')
    shipping_address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship("OrderItems", backref="order")
    payment = db.relationship("Payment", backref="order", uselist=False)


class OrderItems(db.Model):
    order_items_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"))
    quantity = db.Column(db.Integer)
    order_price = db.Column(db.Numeric(10,2))
    subtotal = db.Column(db.Numeric(10,2))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Payment(db.Model):
    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.order_id"))
    amount = db.Column(db.Numeric(10,2))
    method = db.Column(db.String(50))
    status = db.Column(db.Enum("unpaid", "paid"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
