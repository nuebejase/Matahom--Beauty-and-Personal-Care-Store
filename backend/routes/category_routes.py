# routes/category_routes.py

from flask import Blueprint, request, jsonify
from models import db
from models.category_model import Category

category_bp = Blueprint("categories", __name__)

@category_bp.route("/category", methods=["POST"])
def create_category():
    data = request.json
    category = Category(**data)
    db.session.add(category)
    db.session.commit()
    return jsonify(category.to_dict()), 201


@category_bp.route("/category", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return jsonify([c.to_dict() for c in categories])


@category_bp.route("/category/<int:id>", methods=["GET"])
def get_category(id):
    category = Category.query.get_or_404(id)
    return jsonify(category.to_dict())


@category_bp.route("/category/<int:id>", methods=["PUT"])
def update_category(id):
    data = request.json
    category = Category.query.get_or_404(id)

    for key, value in data.items():
        setattr(category, key, value)

    db.session.commit()
    return jsonify(category.to_dict())


@category_bp.route("/category/<int:id>", methods=["DELETE"])
def delete_category(id):
    category = Category.query.get_or_404(id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted"})
