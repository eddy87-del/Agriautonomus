"""Database Configuration"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Asset(db.Model):
    __tablename__ = 'assets'
    
    id = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(255))
    asset_type = db.Column(db.String(50))
    status = db.Column(db.String(50))
    battery_level = db.Column(db.Float)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    last_seen = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Mission(db.Model):
    __tablename__ = 'missions'
    
    id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String(255))
    asset_id = db.Column(db.String(100))
    mission_type = db.Column(db.String(50))
    status = db.Column(db.String(50))
    waypoints = db.Column(db.JSON)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Telemetry(db.Model):
    __tablename__ = 'telemetry'
    
    id = db.Column(db.Integer, primary_key=True)
    asset_id = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    battery_level = db.Column(db.Float)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    altitude = db.Column(db.Float)
    data = db.Column(db.JSON)

class Alert(db.Model):
    __tablename__ = 'alerts'
    
    id = db.Column(db.String(8), primary_key=True)
    alert_type = db.Column(db.String(100))
    message = db.Column(db.Text)
    severity = db.Column(db.String(20))
    asset_id = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
