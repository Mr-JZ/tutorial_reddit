from sqlalchemy.orm import Session
from typing import Optional
from .. import models, schemas

# GET
def get_tutorial(db: Session, tutorial_id: int):
    return db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()

def get_tutorials_by_name(db: Session, name: str, level: int = None, skip: int = 0, limit: int = 100):
    if level:
        return db.query(models.Tutorial).filter(models.Tutorial.name == name and models.Tutorial.level == level).offset(skip).limit(limit).all()
    return db.query(models.Tutorial).filter(models.Tutorial.name == name).offset(skip).limit(limit).all()

def get_tutorials_by_topic(db: Session, topic_id: int, level: int = None, skip: int = 0, limit: int = 100):
    if level:
        return db.query(models.Tutorial).filter(models.Tutorial.topic_id == topic_id and models.Tutorial.level == level).offset(skip).limit(limit).all()
    return db.query(models.Tutorial).filter(models.Tutorial.topic_id == topic_id).offset(skip).limit(limit).all()

def get_tutorials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tutorial).offset(skip).limit(limit).all()
# CREATE
def create_tutorial(db: Session, tutorial: schemas.TutorialCreate, user_id: int):
    db_tutorial =  models.Tutorial(**tutorial.dict(), creator=user_id)
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

# UPDATE
def update_tutorial(db: Session, tutorial_id: int, tutorial: Optional[schemas.TutorialCreate]):
    db_tutorial = get_tutorial(db, tutorial_id=tutorial_id).update()
    if tutorial.name:
        db_tutorial.name = tutorial.name
    if tutorial.topic_id:
        db_tutorial.topic_id = tutorial.topic_id
    if tutorial.level:
        db_tutorial.level = tutorial.level
    if tutorial.description:
        db_tutorial.description = tutorial.description
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

# DELETE
def delete_tutorial(db: Session, tutorial_id: int):
    get_tutorial(db, tutorial_id=tutorial_id).delete(synchronize_session=False)
    db.commit()
