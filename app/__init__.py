from flask import Flask
from app.utils.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
from app.models.bike_specs import Condition, WheelSize, FrameSize


@app.shell_context_processor
def define_context():
    return {"db": db}
