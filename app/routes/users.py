from typing import List
from fastapi import Response, APIRouter, Depends
from pydantic import StrictBool
from sqlmodel import Session, select
from fastapi.exceptions import HTTPException
from app.models import User, UserBase, UserwithPosts
from app.db import get_session

router = APIRouter()
@router.get("/")
def list_users(session: Session = Depends(get_session)) -> List[User]:
    users = session.exec(select(User)).all()
    return users


@router.get("/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)) -> UserwithPosts|None:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/")
def create_user(user: UserBase, session: Session = Depends(get_session)) -> User:
    u=User(name=user.name, surname=user.surname, age=user.age, email=user.email)
    session.add(u)
    session.commit()
    session.refresh(u)
    return u
@router.put("/{user_id}")
def update_user(user: UserBase, user_id: int, session: Session = Depends(get_session)) -> User:
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
def remove_user(user_id: int, response: Response, session: Session = Depends(get_session)) -> StrictBool:
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    response.status_code=404
    return False