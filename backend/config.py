# config.py
import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey123")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecretkey123")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:@localhost/matahomph_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
