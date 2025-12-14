from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import User
from models import db


class AuthService:

    @staticmethod
    def register(name, email, password):
        existing = User.query.filter_by(email=email).first()
        if existing:
            return None, "Email already exists."

        hashed = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed)

        db.session.add(new_user)
        db.session.commit()

        return new_user, None

    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()
        if not user:
            return None, "User not found."

        if not check_password_hash(user.password, password):
            return None, "Incorrect password."

        return user, None
