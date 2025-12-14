import jwt
from datetime import datetime, timedelta
from flask import current_app

def generate_token(payload):
    payload['exp'] = datetime.utcnow()+timedelta(hours=2)
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    return token
def decode_token(token):
    if token.startswith('Bearer'):
        token = token.split(' ')[1]
        decode = jwt.encode(token, current_app.config['SECRET_KEY'], algorithm=['HS256'])
        return decoded