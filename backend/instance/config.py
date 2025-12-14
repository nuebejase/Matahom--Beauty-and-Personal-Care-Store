# instance/config.py
SECRET_KEY = "your_local_secret"
JWT_SECRET_KEY = "your_local_jwt_secret"

# LOCAL DATABASE CONNECTION
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:@localhost/matahomph_db"
