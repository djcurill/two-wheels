from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # intialize plugins
    db.init_app(app)
    migrate.init_app(app, db)

    from app.specifications import bp as specs_bp

    app.register_blueprint(specs_bp, url_prefix="/specs")

    from app.bikes import bp as bikes_bp

    app.register_blueprint(bikes_bp, url_prefix="/bikes")

    return app


from app.specifications.models import Brand, Condition, FrameSize, WheelSize
from app.bikes.models import Bike
