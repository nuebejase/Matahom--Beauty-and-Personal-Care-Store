from models.payment_model import Payment
from models import db


class PaymentService:

    @staticmethod
    def create_payment(order_id, amount, method, status="pending"):
        payment = Payment(
            order_id=order_id,
            amount=amount,
            method=method,
            status=status
        )
        db.session.add(payment)
        db.session.commit()
        return payment

    @staticmethod
    def update_status(payment_id, status):
        payment = Payment.query.get(payment_id)
        if not payment:
            return None

        payment.status = status
        db.session.commit()
        return payment
