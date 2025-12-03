from flask import Blueprint, request, jsonify
from config import db
from models import OrderItems

order_items_routes = Blueprint("order_items_routes", __name__)

# CREATE ORDER ITEM
@order_items_routes.route("/order-items", methods=["POST"])
def create_order_item():
    data = request.json
    item = OrderItems(**data)
    db.session.add(item)
    db.session.commit()
    return jsonify({"message": "Order Item created", "order_items_id": item.order_items_id})

# GET ITEMS BY ORDER
@order_items_routes.route("/order-items/<int:order_id>", methods=["GET"])
def get_order_items(order_id):
    items = OrderItems.query.filter_by(order_id=order_id).all()
    return jsonify([{
        "order_items_id": i.order_items_id,
        "product_id": i.product_id,
        "quantity": i.quantity,
        "order_price": str(i.order_price),
        "subtotal": str(i.subtotal)
    } for i in items])
