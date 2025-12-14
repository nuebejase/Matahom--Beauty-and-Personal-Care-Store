from models.product_model import Product
from models import db


class ProductService:

    @staticmethod
    def get_all():
        return Product.query.all()

    @staticmethod
    def get_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def create(data):
        product = Product(**data)
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(product_id, data):
        product = Product.query.get(product_id)
        if not product:
            return None

        for key, value in data.items():
            setattr(product, key, value)

        db.session.commit()
        return product

    @staticmethod
    def delete(product_id):
        product = Product.query.get(product_id)
        if not product:
            return False
        db.session.delete(product)
        db.session.commit()
        return True
