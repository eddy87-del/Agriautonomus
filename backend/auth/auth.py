"""Authentication and Authorization"""
from functools import wraps
from flask import request, jsonify
from loguru import logger
import os
from datetime import datetime, timedelta
import jwt

SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')

def generate_token(user_id: str, expires_in: int = 3600) -> str:
    """Generate JWT token"""
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(seconds=expires_in),
        'iat': datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def verify_token(token: str) -> dict:
    """Verify JWT token"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        logger.warning("Token expired")
        return None
    except jwt.InvalidTokenError:
        logger.warning("Invalid token")
        return None

def token_required(f):
    """Decorator for token verification"""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'message': 'Invalid token format'}), 401
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        
        payload = verify_token(token)
        if not payload:
            return jsonify({'message': 'Invalid or expired token'}), 401
        
        return f(payload, *args, **kwargs)
    
    return decorated

def login(username: str, password: str) -> str:
    """User login"""
    # TODO: Verify credentials against database
    logger.info(f"User logged in: {username}")
    return generate_token(username)
