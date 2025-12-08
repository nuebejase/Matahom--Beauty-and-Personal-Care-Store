from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db, Inventory

inventory_routes = Blueprint('inventory_routes', __name__)

# GET all inventory items
@inventory_routes.route('/inventory', methods=['GET'])
def get_inventory():
    inventory_list = Inventory.query.all()
    result = []
    for item in inventory_list:
        result.append({
            "inventory_id": item.inventory_id,
            "product_id": item.product_id,
            "quantity": item.quantity,
            "updated_at": item.updated_at
        })
    return jsonify(result), 200

# GET a single inventory item by id
@inventory_routes.route('/inventory/<int:id>', methods=['GET'])
def get_inventory_item(id):
    item = Inventory.query.get(id)
    if not item:
        return jsonify({"message": "Inventory item not found"}), 404

    return jsonify({
        "inventory_id": item.inventory_id,
        "product_id": item.product_id,
        "quantity": item.quantity,
        "updated_at": item.updated_at
    }), 200

# CREATE new inventory item
@inventory_routes.route('/inventory', methods=['POST'])
def create_inventory():
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not product_id or quantity is None:
        return jsonify({"message": "product_id and quantity are required"}), 400

    new_item = Inventory(product_id=product_id, quantity=quantity)
    db.session.add(new_item)
    db.session.commit()

    return jsonify({
        "message": "Inventory item created",
        "inventory_id": new_item.inventory_id
    }), 201

# UPDATE an inventory item
@inventory_routes.route('/inventory/<int:id>', methods=['PUT'])
def update_inventory(id):
    item = Inventory.query.get(id)
    if not item:
        return jsonify({"message": "Inventory item not found"}), 404

    data = request.get_json()
    item.product_id = data.get("product_id", item.product_id)
    item.quantity = data.get("quantity", item.quantity)
    item.updated_at = datetime.utcnow()

    db.session.commit()

    return jsonify({"message": "Inventory item updated"}), 200

# DELETE an inventory item
@inventory_routes.route('/inventory/<int:id>', methods=['DELETE'])
def delete_inventory(id):
    item = Inventory.query.get(id)
    if not item:
        return jsonify({"message": "Inventory item not found"}), 404

    db.session.delete(item)
    db.session.commit()

    return jsonify({"message": "Inventory item deleted"}), 200
