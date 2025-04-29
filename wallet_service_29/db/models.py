from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Wallet(Base):
    __tablename__ = 'wallets'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), nullable=False)
    card_id = Column(String(16), unique=True, nullable=False)
    status = Column(String(20), default='inactive')
    created_at = Column(DateTime, default=datetime.now())
    activated_at = Column(DateTime, nullable=True)
