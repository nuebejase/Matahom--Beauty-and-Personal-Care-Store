from models.category_model import Category
from models import db


class CategoryService:

    @staticmethod
    def get_all():
        return Category.query.all()

    @staticmethod
    def get_by_id(category_id):
        return Category.query.get(category_id)

    @staticmethod
    def create(data):
        category = Category(**data)
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def update(category_id, data):
        category = Category.query.get(category_id)
        if not category:
            return None

        for key, value in data.items():
            setattr(category, key, value)

        db.session.commit()
        return category

    @staticmethod
    def delete(category_id):
        category = Category.query.get(category_id)
        if not category:
            return False
        db.session.delete(category)
        db.session.commit()
        return True
