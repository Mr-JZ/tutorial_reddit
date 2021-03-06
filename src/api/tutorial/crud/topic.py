from sqlalchemy.orm import Session
from api.tutorial import models, schemas

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
def update_topic(db: Session, topic_id: int, topic: schemas.TopicCreate):
    db_topic = get_topic(db, topic_id=topic_id)
    db_topic.name = topic.name
    db.commit()
    db.refresh(db_topic)
    return db_topic

# DELETE
def delete_topic(db: Session, topic_id: int):
    db.query(models.Topic).filter(models.Topic.id == id).delete()
    db.commit()
