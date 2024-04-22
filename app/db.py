import os
from sqlmodel import Session, SQLModel, create_engine
from dotenv import load_dotenv

load_dotenv()

db_url=os.environ.get("DATABASE_URL")
print(f"db_url: {db_url}")
engine = create_engine(db_url, echo=True)

from .models import User, Post
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
