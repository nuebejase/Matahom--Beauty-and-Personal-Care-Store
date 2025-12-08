from flask import Flask
from config import Config, db
from models import *

from routes.user_routes import user_routes
from routes.product_routes import product_routes
from routes.order_routes import order_routes
from routes.category_routes import category_routes
from routes.order_items_routes import order_items_routes
from routes.inventory_routes import inventory_routes
from routes.payment_routes import payment_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Register routes
app.register_blueprint(user_routes)
app.register_blueprint(product_routes)
app.register_blueprint(order_routes)
app.register_blueprint(category_routes)
app.register_blueprint(order_items_routes)
app.register_blueprint(inventory_routes)
app.register_blueprint(payment_routes)

@app.route("/")
def index():
    return {"message": "Matahom API Running"}

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)