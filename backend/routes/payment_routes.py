# routes/payment_routes.py

from flask import Blueprint, request, jsonify
from models import db
from models.payment_model import Payment

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/payments", methods=["POST"])
def create_payment():
    data = request.json
    payment = Payment(**data)
    db.session.add(payment)
    db.session.commit()
    return jsonify(payment.to_dict()), 201


@payment_bp.route("/payments/<int:order_id>", methods=["GET"])
def get_payment(order_id):
    payment = Payment.query.filter_by(order_id=order_id).first()
    if not payment:
        return jsonify({"message": "No payment found"}), 404
    return jsonify(payment.to_dict())
