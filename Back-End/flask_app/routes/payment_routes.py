from flask import Blueprint, request, jsonify
from datetime import datetime
from models import db, Payment

payment_routes = Blueprint("payment_routes", __name__)

# ---------------------------
# GET ALL PAYMENTS
# ---------------------------
@payment_routes.route("/payments", methods=["GET"])
def get_payments():
    payments = Payment.query.all()
    result = []
    for p in payments:
        result.append({
            "payment_id": p.payment_id,
            "order_id": p.order_id,
            "amount": str(p.amount),
            "method": p.method,
            "status": p.status,
            "created_at": p.created_at
        })
    return jsonify(result), 200


# ---------------------------
# GET PAYMENT BY ID
# ---------------------------
@payment_routes.route("/payments/<int:id>", methods=["GET"])
def get_payment(id):
    payment = Payment.query.get(id)
    if not payment:
        return jsonify({"message": "Payment not found"}), 404

    return jsonify({
        "payment_id": payment.payment_id,
        "order_id": payment.order_id,
        "amount": str(payment.amount),
        "method": payment.method,
        "status": payment.status,
        "created_at": payment.created_at
    }), 200


# ---------------------------
# CREATE PAYMENT
# ---------------------------
@payment_routes.route("/payments", methods=["POST"])
def create_payment():
    data = request.get_json()

    required = ["order_id", "amount", "method", "status"]
    if not all(k in data for k in required):
        return jsonify({"message": "order_id, amount, method, and status are required"}), 400
    
    if data["status"] not in ["unpaid", "paid"]:
        return jsonify({"message": "status must be 'unpaid' or 'paid'"}), 400

    payment = Payment(
        order_id=data["order_id"],
        amount=data["amount"],
        method=data["method"],
        status=data["status"]
    )
    db.session.add(payment)
    db.session.commit()

    return jsonify({
        "message": "Payment created",
        "payment_id": payment.payment_id
    }), 201


# ---------------------------
# UPDATE PAYMENT
# ---------------------------
@payment_routes.route("/payments/<int:id>", methods=["PUT"])
def update_payment(id):
    payment = Payment.query.get(id)
    if not payment:
        return jsonify({"message": "Payment not found"}), 404

    data = request.get_json()

    if "status" in data:
        if data["status"] not in ["unpaid", "paid"]:
            return jsonify({"message": "status must be 'unpaid' or 'paid'"}), 400

    payment.order_id = data.get("order_id", payment.order_id)
    payment.amount = data.get("amount", payment.amount)
    payment.method = data.get("method", payment.method)
    payment.status = data.get("status", payment.status)

    db.session.commit()

    return jsonify({"message": "Payment updated"}), 200


# ---------------------------
# DELETE PAYMENT
# ---------------------------
@payment_routes.route("/payments/<int:id>", methods=["DELETE"])
def delete_payment(id):
    payment = Payment.query.get(id)
    if not payment:
        return jsonify({"message": "Payment not found"}), 404

    db.session.delete(payment)
    db.session.commit()

    return jsonify({"message": "Payment deleted"}), 200
