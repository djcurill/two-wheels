from multiprocessing import Condition
from app import create_app

app = create_app()
with app.app_context():
    print(Condition.query.all())
