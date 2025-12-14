# models/inventory_model.py
from models import db
from datetime import datetime

class Inventory(db.Model):
    __tablename__ = "inventory"

    inventory_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.product_id"), unique=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "inventory_id": self.inventory_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "updated_at": self.updated_at,
        }
