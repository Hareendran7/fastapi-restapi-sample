from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Pambi", 
        last_name='Paubi',
        gender= Gender.female,
        roles=[Role.student]
    ),
    User(
        id=uuid4(), 
        first_name="Alex", 
        last_name='Pandiyan',
        gender= Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
def root():
    return {"Hello": "Hareendran"}

@app.get("/api/v1/users")
def fetch_users():
    return db

@app.post("/api/v1/users")
def add_user(user: User):
    db.append(user)
    return {'id': user.id}