# routes/inventory_routes.py

from flask import Blueprint, request, jsonify
from models import db
from models.inventory_model import Inventory

inventory_bp = Blueprint("inventory", __name__)

# UPDATE STOCK
@inventory_bp.route("/inventory", methods=["POST"])
def update_stock():
    data = request.json
    product_id = data.get("product_id")
    qty_change = data.get("qty_change")

    inv = Inventory.query.filter_by(product_id=product_id).first()

    # Auto-create if not existing
    if not inv:
        inv = Inventory(product_id=product_id, quantity=0)
        db.session.add(inv)

    inv.quantity += qty_change
    db.session.commit()

    return jsonify(inv.to_dict())



# GET STOCK OF PRODUCT
@inventory_bp.route("/inventory/<int:product_id>", methods=["GET"])
def get_stock(product_id):
    inv = Inventory.query.filter_by(product_id=product_id).first()

    if not inv:
        # Option: auto-create with 0
        inv = Inventory(product_id=product_id, quantity=0)
        db.session.add(inv)
        db.session.commit()

    return jsonify(inv.to_dict())
