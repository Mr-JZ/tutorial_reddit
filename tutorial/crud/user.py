from sqlalchemy.orm import Session
from typing import Optional
from .. import models, schemas
from tutorial.hashing import Hash

# GET
def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def get_user_by_identification(db: Session, identification: str):
    return db.query(models.User).filter(models.User.identification == identification).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
# CREATE
def create_user(db: Session, user: schemas.UserCreate):
    password = Hash.bcrypt(user.password)
    db_user = models.User(identification = user.identification, password = password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
# UPDATE
# DELETE
