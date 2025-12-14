from models.order_items_model import OrderItem
from models import db


class OrderItemsService:

    @staticmethod
    def add_item(order_id, product_id, qty, price):
        item = OrderItem(
            order_id=order_id,
            product_id=product_id,
            quantity=qty,
            price=price
        )
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def get_items(order_id):
        return OrderItem.query.filter_by(order_id=order_id).all()

    @staticmethod
    def remove_item(item_id):
        item = OrderItem.query.get(item_id)
        if not item:
            return False
        db.session.delete(item)
        db.session.commit()
        return True
