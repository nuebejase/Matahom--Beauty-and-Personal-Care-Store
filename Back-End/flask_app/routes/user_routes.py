from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

user_routes = Blueprint("user_routes", __name__)


# -------------------------------
# REGISTER USER
# -------------------------------
@user_routes.route("/register", methods=["POST"])
def register():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    address = data.get("address")
    role = data.get("role", "customer")  # default user role

    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    # Hash password
    hashed_password = generate_password_hash(password)

    new_user = User(
        name=name,
        email=email,
        password=hashed_password,
        address=address,
        role=role
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201



# -------------------------------
# LOGIN USER
# -------------------------------
@user_routes.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Email not found"}), 404

    if not check_password_hash(user.password, password):
        return jsonify({"error": "Incorrect password"}), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "user_id": user.user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }
    }), 200



# -------------------------------
# GET ALL USERS
# -------------------------------
@user_routes.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "user_id": u.user_id,
            "name": u.name,
            "email": u.email,
            "address": u.address,
            "role": u.role
        }
        for u in users
    ])



# -------------------------------
# UPDATE USER
# -------------------------------
@user_routes.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.json

    # If password update is included
    if "password" in data:
        data["password"] = generate_password_hash(data["password"])

    for key, value in data.items():
        setattr(user, key, value)

    db.session.commit()
    return jsonify({"message": "User updated"}), 200



# -------------------------------
# DELETE USER
# -------------------------------
@user_routes.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200
