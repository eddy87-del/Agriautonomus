"""Utility Functions"""
from datetime import datetime
import uuid

def generate_id(prefix: str = '') -> str:
    """Generate unique ID"""
    unique_id = str(uuid.uuid4())[:8]
    return f"{prefix}_{unique_id}" if prefix else unique_id

def get_timestamp() -> str:
    """Get current timestamp"""
    return datetime.utcnow().isoformat()

def format_response(success: bool, data: dict = None, message: str = ''):
    """Format API response"""
    return {
        'success': success,
        'data': data or {},
        'message': message,
        'timestamp': get_timestamp()
    }

def calculate_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two coordinates using Haversine formula"""
    from math import radians, cos, sin, asin, sqrt
    
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km
