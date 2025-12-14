from flask import Flask
from flask_cors import CORS
from models import db
from routes import all_blueprints
from config import Config

# JWT
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Load main config
    app.config.from_object(Config)

    # Load instance config (DB credentials)
    app.config.from_pyfile("config.py", silent=True)

    # Enable CORS for Angular frontend
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Initialize extensions
    db.init_app(app)
    JWTManager(app)

    # Register all blueprints under /api prefix
    for bp in all_blueprints:
        app.register_blueprint(bp, url_prefix="/api")

    @app.route("/")
    def root():
        return {"message": "Matahom API is running"}

    return app


# WSGI entry point
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
