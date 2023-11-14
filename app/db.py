import os
from sqlmodel import Field, Session, SQLModel, create_engine, select


db_url=os.environ.get("DATABASE_URL")
engine = create_engine(db_url, echo=True)

from .models import User, UserBase
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)