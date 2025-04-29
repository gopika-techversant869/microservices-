from app.db.db_handler import db
from datetime import datetime

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    card_number = db.Column(db.String(16), unique=True, nullable=False)
    status = db.Column(db.String(20), default='inactive')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    activated_at = db.Column(db.DateTime, nullable=True)
    expiry_date = db.Column(db.DateTime, nullable=True)
    card_type = db.Column(db.String(25), nullable=True)
    card_network = db.Column(db.String(20),nullable=True)
    card_variant = db.Column(db.String(20),nullable=True)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(20), nullable = True)