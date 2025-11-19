from flask import Blueprint, request, jsonify
from models import db, Order, OrderItems, Product

order_routes = Blueprint("order_routes", __name__)

@order_routes.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    user_id = data["user_id"]
    shipping_address = data["shipping_address"]
    items = data["items"]

    total = 0
    order = Order(user_id=user_id, shipping_address=shipping_address)
    db.session.add(order)
    db.session.commit()

    # Add ordered items
    for item in items:
        product = Product.query.get(item["product_id"])

        subtotal = float(product.price) * item["quantity"]
        total += subtotal

        # Insert into order items
        order_item = OrderItems(
            order_id=order.order_id,
            product_id=product.product_id,
            quantity=item["quantity"],
            order_price=product.price,
            subtotal=subtotal
        )
        db.session.add(order_item)

        # Reduce stock
        product.stock -= item["quantity"]

    order.total_amount = total
    db.session.commit()

    return jsonify({"message": "Order placed", "order_id": order.order_id})
