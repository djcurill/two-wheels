from flask import Blueprint

bp = Blueprint("specifications", __name__)

from app.specifications import routes
from app.specifications import models
