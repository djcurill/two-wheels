from multiprocessing import Condition
from app import create_app
from app.specifications.models import Condition

app = create_app()
with app.app_context():
    print(Condition.query.all())
