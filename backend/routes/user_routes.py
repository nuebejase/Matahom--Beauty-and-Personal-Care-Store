# routes/user_routes.py

from flask import Blueprint, request, jsonify
from models import db
from models.user_model import User

user_bp = Blueprint("user", __name__)

# CREATE USER
@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201


# READ ALL USERS
@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([u.to_dict() for u in users])


# READ ONE USER
@user_bp.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


# UPDATE USER
@user_bp.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    data = request.json
    user = User.query.get_or_404(id)

    for key, value in data.items():
        setattr(user, key, value)

    db.session.commit()
    return jsonify(user.to_dict())


# DELETE USER
@user_bp.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"})
