from typing import List
from fastapi import APIRouter
from sqlmodel import Session, select
from app.models import PostBase, Post, User
from app.db import engine


router = APIRouter()

@router.get("/{user_id}")
def list_users_posts(user_id: int) -> List[Post]:
    with Session(engine) as session:
        posts = session.exec(select(Post).where(Post.user_id == user_id)).all()
        return posts

@router.post("/{user_id}")
def create_post(user_id: int, post: PostBase) -> Post:
    try:
        with Session(engine) as session:
            u=session.get(User, user_id)
            p=Post(title=post.title, body=post.body, user_id=user_id)
            p.user_id=u.id
            session.add(p)
            session.commit()
            session.refresh(p)
            return p
    except:
        raise HTTPException(status_code=404, detail="User not found")
