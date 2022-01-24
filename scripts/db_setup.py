from app import create_app
from app.database import init_db, wipe_db

app = create_app()
with app.app_context():
    wipe_db()
    init_db()
