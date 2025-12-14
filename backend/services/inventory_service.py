from models.inventory_model import Inventory
from models import db


class InventoryService:

    @staticmethod
    def get_all():
        return Inventory.query.all()

    @staticmethod
    def get_by_product(product_id):
        return Inventory.query.filter_by(product_id=product_id).first()

    @staticmethod
    def add_stock(product_id, qty):
        stock = Inventory.query.filter_by(product_id=product_id).first()
        if stock:
            stock.quantity += qty
        else:
            stock = Inventory(product_id=product_id, quantity=qty)

        db.session.add(stock)
        db.session.commit()
        return stock

    @staticmethod
    def reduce_stock(product_id, qty):
        stock = Inventory.query.filter_by(product_id=product_id).first()
        if not stock or stock.quantity < qty:
            return None

        stock.quantity -= qty
        db.session.commit()
        return stock
