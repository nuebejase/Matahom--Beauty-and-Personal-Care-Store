from models.order_model import Order
from models import db


class OrderService:

    @staticmethod
    def create_order(user_id, total_amount):
        new_order = Order(user_id=user_id, total_amount=total_amount)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def get_order(order_id):
        return Order.query.get(order_id)

    @staticmethod
    def get_orders_by_user(user_id):
        return Order.query.filter_by(user_id=user_id).all()
