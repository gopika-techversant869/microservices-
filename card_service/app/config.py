

class Config:

    DB_USERNAME = "postgres"
    DB_PASSWORD = "Gopika%4097"
    DB_HOST = "localhost"
    DB_PORT = "3306"
    DB_NAME = "card_db"

    # SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False