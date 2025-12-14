from functools import wraps
from flask import request, jsonify
from utils.jwt_helper import decode_token


def jwt_required(role=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            token = request.headers.get('Authorization')
            if not token:
                return jsonify({'message': 'Token is missing'}), 401
            try:
                data = decode_token(token)
                if role and data.get('role') != role:
                    return jsonify({'message': 'Unauthorized access'}), 403
                request.user = data
            except Exception as e:
                return jsonify({'message': 'Invalid or expired token'}), 401
            return f(*args, **kwargs)
        return wrapper
    return decorator
        