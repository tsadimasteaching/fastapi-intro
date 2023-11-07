from typing import Optional, List

from fastapi import FastAPI, Response
from pydantic import BaseModel, StrictBool

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str


user1 = User(id=1, name="Argiris",surname="Tsadimas", email="tsadimas@gmail.com")
user2 = User(id=2, name="Jim",surname="Tone", email="jim.tone@gmail.com")

users = []
users.append(user1)
users.append(user2)


@app.get("/user")
def read_root():
    return users


@app.get("/user/{user_id}")
def get_user(user_id: int) -> List[User]:
    result = list(filter(lambda x: x.id == user_id, users))
    return result

@app.post("/user")
def create_user(user: User) -> User:
    users.append(user)
    return user

@app.delete("/user/{user_id}")
def remove_user(user_id: int, response: Response) -> StrictBool:
    print(user_id)
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return True
    response.status_code=404
    return False