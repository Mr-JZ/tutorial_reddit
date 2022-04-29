from sqlalchemy.orm import Session
from typing import Optional
from .. import models, schemas

# GET
def get_topic(db: Session, topic_id: id):
    return db.query(models.Topic).filter(models.Topic.id == topic_id).first()

def get_topics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).offset(skip).limit(limit).all()

def get_topic_by_name(db: Session, name: str):
    return db.query(models.Topic).filter(models.Topic.name == name).first()
# CREATE
def create_topic(db: Session, topic: schemas.TopicCreate, user_id: int):
    db_topic = models.Topic(**topic.dict(), user_id=user_id)
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

# UPDATE
# DELETE
