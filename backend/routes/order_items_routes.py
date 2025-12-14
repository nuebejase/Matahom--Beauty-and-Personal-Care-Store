# routes/order_items_routes.py

from flask import Blueprint, request, jsonify
from models import db
from models.order_items_model import OrderItem

order_items_bp = Blueprint("order_items", __name__)

@order_items_bp.route("/orderitems", methods=["POST"])
def add_item():
    data = request.json
    item = OrderItem(**data)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201


@order_items_bp.route("/orderitems/<int:order_id>", methods=["GET"])
def get_items(order_id):
    items = OrderItem.query.filter_by(order_id=order_id).all()
    return jsonify([i.to_dict() for i in items])


@order_items_bp.route("/orderitems/<int:id>", methods=["PUT"])
def update_item(id):
    data = request.json
    item = OrderItem.query.get_or_404(id)

    for key, value in data.items():
        setattr(item, key, value)

    db.session.commit()
    return jsonify(item.to_dict())


@order_items_bp.route("/orderitems/<int:id>", methods=["DELETE"])
def delete_item(id):
    item = OrderItem.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item removed"})
