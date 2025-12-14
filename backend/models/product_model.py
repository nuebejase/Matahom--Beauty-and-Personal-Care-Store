# models/product_model.py
from models import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "products"

    product_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.category_id"))

    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, default=0)
    image_url = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    inventory = db.relationship("Inventory", backref="product", uselist=False)
    order_items = db.relationship("OrderItem", backref="product", lazy=True)

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "category_id": self.category_id,
            "name": self.name,
            "description": self.description,
            "price": float(self.price),
            "stock": self.stock,
            "image_url": self.image_url,
            "created_at": self.created_at,
        }
