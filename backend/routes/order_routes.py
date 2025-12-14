# routes/order_routes.py

from flask import Blueprint, request, jsonify
from models import db
from models.order_model import Order

order_bp = Blueprint("order", __name__)

# CREATE ORDER
@order_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return jsonify(order.to_dict()), 201


# GET ALL ORDERS
@order_bp.route("/orders", methods=["GET"])
def get_orders():
    orders = Order.query.all()
    return jsonify([o.to_dict() for o in orders])


# GET ONE ORDER
@order_bp.route("/orders/<int:id>", methods=["GET"])
def get_order(id):
    order = Order.query.get_or_404(id)
    return jsonify(order.to_dict())


# UPDATE ORDER STATUS
@order_bp.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):
    data = request.json
    order = Order.query.get_or_404(id)

    for key, value in data.items():
        setattr(order, key, value)

    db.session.commit()
    return jsonify(order.to_dict())
