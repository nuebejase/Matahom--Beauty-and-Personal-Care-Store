from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User

user_routes = Blueprint("user_routes", __name__)

# -------------------------------
# REGISTER USER (admin or customer)
# -------------------------------
@user_routes.route("/register", methods=["POST"])
def register():
    try:
        data = request.json

        required = ["name", "email", "password", "address"]
        if not all(field in data for field in required):
            return jsonify({"error": "Missing required fields"}), 400

        # Default role is customer
        role = data.get("role", "customer")
        if role not in ["admin", "customer"]:
            return jsonify({"error": "Invalid role value"}), 400

        # Check duplicate email
        if User.query.filter_by(email=data["email"]).first():
            return jsonify({"error": "Email already registered"}), 409

        new_user = User(
            name=data["name"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
            address=data["address"],
            role=role
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500



# -------------------------------
# LOGIN USER
# -------------------------------
@user_routes.route("/login", methods=["POST"])
def login():
    try:
        data = request.json
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

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

    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500



# -------------------------------
# GET ALL USERS (ADMIN ONLY)
# -------------------------------
@user_routes.route("/users", methods=["GET"])
def get_users():
    try:
        role = request.args.get("role")

        # require admin role
        if role != "admin":
            return jsonify({"error": "Unauthorized, admin only"}), 403
        
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
        ]), 200
    
    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500



# -------------------------------
# UPDATE USER (ADMIN OR SELF)
# -------------------------------
@user_routes.route("/users/<int:id>", methods=["PUT"])
def update_user(id):
    try:
        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        data = request.json
        requester_role = data.get("requester_role")
        requester_id = data.get("requester_id")

        # only admin OR the user himself can update
        if requester_role != "admin" and requester_id != id:
            return jsonify({"error": "Unauthorized"}), 403

        # Prevent non-admin from changing role
        if requester_role != "admin" and "role" in data:
            return jsonify({"error": "Only admin can change roles"}), 403

        # Hash password if changing
        if "password" in data:
            data["password"] = generate_password_hash(data["password"])

        for key, value in data.items():
            if key in ["requester_role", "requester_id"]:
                continue
            setattr(user, key, value)

        db.session.commit()
        return jsonify({"message": "User updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500



# -------------------------------
# DELETE USER (ADMIN ONLY)
# -------------------------------
@user_routes.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        role = request.args.get("role")

        # delete user is admin only
        if role != "admin":
            return jsonify({"error": "Unauthorized, admin only"}), 403

        user = User.query.get(id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted"}), 200

    except Exception as e:
        return jsonify({"error": "Server error", "details": str(e)}), 500
