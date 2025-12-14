# routes/product_routes.py

from flask import Blueprint, request, jsonify
from models import db
from models.product_model import Product

product_bp = Blueprint("product", __name__)

# CREATE PRODUCT
@product_bp.route("/products", methods=["POST"])
def create_product():
    data = request.json
    product = Product(**data)
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201


# GET ALL PRODUCTS
@product_bp.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([p.to_dict() for p in products])


# GET ONE PRODUCT
@product_bp.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict())


# UPDATE PRODUCT
@product_bp.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.json
    product = Product.query.get_or_404(id)

    for key, value in data.items():
        setattr(product, key, value)

    db.session.commit()
    return jsonify(product.to_dict())


# DELETE PRODUCT
@product_bp.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"})
