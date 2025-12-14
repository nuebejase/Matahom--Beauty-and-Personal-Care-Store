# models/payment_model.py
from models import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = "payments"

    payment_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.order_id"), unique=True, nullable=False)

    amount = db.Column(db.Numeric(10, 2), nullable=False)
    method = db.Column(db.String(50))  # e.g. GCash, Cash On Delivery
    status = db.Column(db.Enum("pending", "paid", "failed"), default="pending")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "order_id": self.order_id,
            "amount": float(self.amount),
            "method": self.method,
            "status": self.status,
            "created_at": self.created_at,
        }
