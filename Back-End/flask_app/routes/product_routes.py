from flask import Blueprint, request, jsonify
from models import db, Product, Inventory

product_routes = Blueprint("product_routes", __name__)

@product_routes.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            "product_id": p.product_id,
            "name": p.name,
            "price": str(p.price),
            "stock": p.stock,
            "category_id": p.category_id
        } for p in products
    ])  


@product_routes.route("/products", methods=["POST"])
def create_product():
    data = request.json
    product = Product(**data)
    db.session.add(product)
    db.session.commit()

    # Create inventory entry automatically
    inv = Inventory(product_id=product.product_id, quantity=product.stock)
    db.session.add(inv)
    db.session.commit()

    return jsonify({"message": "Product created with inventory"})


@product_routes.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json

    for key, value in data.items():
        setattr(product, key, value)

    db.session.commit()
    return jsonify({"message": "Product updated"})


@product_routes.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)

    # Delete inventory first
    if product.inventory:
        db.session.delete(product.inventory)

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product & inventory deleted"})
