from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List, ForwardRef


class UserBase(SQLModel):
    name: str = Field(index=True)
    surname: str
    age: Optional[int] = Field(default=None, index=True)
    email: str
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    posts: List["Post"] = Relationship(back_populates="user")

class UserRead(UserBase):
    id: int

class PostBase(SQLModel):
    title: str
    body: str
    user_id: int = Field(foreign_key="user.id")


class Post(PostBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional[User] = Relationship(back_populates="posts")

class PostRead(PostBase):
    id: int

class UserwithPosts(UserRead):
    posts: List[PostRead] = []

class PostwithUser(PostRead):
    user: Optional[UserRead] = None


