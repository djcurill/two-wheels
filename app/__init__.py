from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # intialize plugins
    db.init_app(app)
    migrate.init_app(app, db)

    from app.specifications import bp as specs_bp

    app.register_blueprint(specs_bp, url_prefix="/specs")

    return app
