from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

# Replace these with your actual values
DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()

