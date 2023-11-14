from fastapi import FastAPI
from app.routes.users import router as userrouter
from .db import create_db_and_tables



app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(userrouter, prefix='/user', tags=['User'])

