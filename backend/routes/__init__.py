# routes/__init__.py

from .auth_routes import auth_bp
from .user_routes import user_bp
from .product_routes import product_bp
from .category_routes import category_bp
from .order_routes import order_bp
from .order_items_routes import order_items_bp
from .payment_routes import payment_bp
from .inventory_routes import inventory_bp

# export list for app.py
all_blueprints = [
    auth_bp,
    user_bp,
    product_bp,
    category_bp,
    order_bp,
    order_items_bp,
    payment_bp,
    inventory_bp
]
