from flask import Blueprint, request, jsonify
from config import db
from models import Category

category_routes = Blueprint("category_routes", __name__)

# CREATE CATEGORY
@category_routes.route("/categories", methods=["POST"])
def create_category():
    data = request.json
    category = Category(**data)
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": "Category created", "category_id": category.category_id})

# READ ALL CATEGORIES
@category_routes.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return jsonify([{
        "category_id": c.category_id,
        "name": c.name,
        "description": c.description
    } for c in categories])

# READ SINGLE CATEGORY
@category_routes.route("/categories/<int:category_id>", methods=["GET"])
def get_category(category_id):
    category = Category.query.get_or_404(category_id)
    return jsonify({
        "category_id": category.category_id,
        "name": category.name,
        "description": category.description
    })

# UPDATE CATEGORY
@category_routes.route("/categories/<int:category_id>", methods=["PUT"])
def update_category(category_id):
    category = Category.query.get_or_404(category_id)
    data = request.json

    for key, value in data.items():
        setattr(category, key, value)

    db.session.commit()
    return jsonify({"message": "Category updated"})

# DELETE CATEGORY
@category_routes.route("/categories/<int:category_id>", methods=["DELETE"])
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return jsonify({"message": "Category deleted"})
