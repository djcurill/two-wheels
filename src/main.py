from dotenv import load_dotenv
from sqlalchemy import create_engine
import os


load_dotenv()
eng = create_engine(os.getenv("DATABASE_URI"))
print(eng)
