# models/order_items_model.py
from models import db
from datetime import datetime

class OrderItem(db.Model):
    __tablename__ = "order_items"

    order_items_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), nullable=False)

    quantity = db.Column(db.Integer, nullable=False)
    order_price = db.Column(db.Numeric(10, 2), nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "order_items_id": self.order_items_id,
            "order_id": self.order_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "order_price": float(self.order_price),
            "subtotal": float(self.subtotal),
            "created_at": self.created_at,
        }
