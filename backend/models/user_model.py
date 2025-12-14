# models/user_model.py
from models import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255))
    role = db.Column(db.Enum("owner", "customer"), default="customer")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    orders = db.relationship("Order", backref="user", lazy=True)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "address": self.address,
            "role": self.role,
            "created_at": self.created_at,
        }
