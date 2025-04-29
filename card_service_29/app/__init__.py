from flask import Flask
from app.db.db_handler import init_db
from app.config import Config


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    init_db(app)
    # db.init_app(app)

    from app.route import card_bp
    app.register_blueprint(card_bp, url_prefix="/api")
    return app
