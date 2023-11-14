from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class UserBase(SQLModel):
    name: str = Field(index=True)
    surname: str
    age: Optional[int] = Field(default=None, index=True)
    email: str
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


