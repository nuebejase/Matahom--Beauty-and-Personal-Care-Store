# models/order_model.py
from models import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), nullable=False)

    total_amount = db.Column(db.Numeric(10, 2), nullable=False)
    status = db.Column(db.Enum("pending", "shipped", "delivered", "cancelled"), default="pending")
    shipping_address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship("OrderItem", backref="order", lazy=True)
    payment = db.relationship("Payment", backref="order", uselist=False)

    def to_dict(self):
        return {
            "order_id": self.order_id,
            "user_id": self.user_id,
            "total_amount": float(self.total_amount),
            "status": self.status,
            "shipping_address": self.shipping_address,
            "created_at": self.created_at,
        }
