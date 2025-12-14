from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user_model import User
from .category_model import Category
from .product_model import Product
from .inventory_model import Inventory
from .order_model import Order
from .order_items_model import OrderItem
from .payment_model import Payment
