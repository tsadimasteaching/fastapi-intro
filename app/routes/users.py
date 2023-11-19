from typing import Optional, List
import os
from fastapi import FastAPI, Response, APIRouter
from pydantic import BaseModel, StrictBool
from sqlmodel import Field, Session, SQLModel, create_engine, select
from sqlalchemy.orm import selectinload
from fastapi.exceptions import HTTPException
from app.models import User, UserBase, UserwithPosts
from app.db import engine

router = APIRouter()
@router.get("/")
def list_users() -> List[User]:
    with Session(engine) as session:
        heroes = session.exec(select(User)).all()
        return heroes


@router.get("/{user_id}")
def get_user(user_id: int) -> UserwithPosts|None:
    try:
        with Session(engine) as session:
            user = session.exec(select(User).options(selectinload(User.posts)).where(User.id == user_id)).first()
            return user

    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/")
def create_user(user: UserBase) -> User:
    with Session(engine) as session:
        u=User(name=user.name, surname=user.surname, age=user.age, email=user.email)
        session.add(u)
        session.commit()
        session.refresh(u)
        return u
@router.put("/{user_id}")
def update_user(user: UserBase, user_id: int) -> User:
    with Session(engine) as session:
        u = session.get(User, user_id)
        if u:
            u.name=user.name
            u.surname=user.surname
            u.age=user.age
            u.email=user.email
            session.add(u)
            session.commit()
            session.refresh(u)
            return u
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}")
def remove_user(user_id: int, response: Response) -> StrictBool:
    with Session(engine) as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
    response.status_code=404
    return False