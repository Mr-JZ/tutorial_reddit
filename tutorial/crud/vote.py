from sqlalchemy.orm import Session
from typing import Optional
from .. import models, schemas

# GET
def get_vote(db: Session, vote_id: int = 0):
    return db.query(models.Vote).filter(models.Vote.id == vote_id).first()

def get_vote_by_user_and_tutorial_id(db: Session, user_id: int, tutorial_id:int):
    return db.query(models.Vote).filter(models.Vote.user_id == user_id and models.Vote.tutorial_id == tutorial_id).first()

def get_votes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vote).offset(skip).limit(limit).all()

def get_votes_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Vote).filter(models.Vote.user_id == user_id).offset(skip).limit(limit).all()

def get_votes_by_tutorial(db: Session, tutorial_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Vote).filter(models.Vote.tutorial_id == tutorial_id).offset(skip).limit(limit).all()
# CREATE
def create_vote(db: Session, vote: schemas.VoteCreate, user_id: int, tutorial_id: int):
    db_vote = models.Vote(**vote.dict(), user_id = user_id, tutorial_id = tutorial_id)
    db.add(db_vote)
    db.commit()
    db.refresh(db_vote)
    return db_vote
# UPDATE
def update_vote(db: Session, vote_id: int):
    db_vote = get_vote(db, vote_id=vote_id)
    db_vote.up = not db_vote.up
    db.commit()
    db.refresh(db_vote)
    return db_vote
# DELETE
def delete_vote(db: Session, vote_id: int):
    get_vote(db, vote_id=vote_id).vote(synchronize_session=False)
    db.commit()
