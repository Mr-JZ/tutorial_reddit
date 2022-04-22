from sqlalchemy.orm import Session

from . import models, schemas

# --------------------------------------------------------------------------
# User
# --------------------------------------------------------------------------

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_accesslevel(db: Session, user_id: int):
    return db.query(models.User.access_level).filter(models.User.id == user_id).first()

def get_user_by_identification(db: Session, identification: str):
    return db.query(models.User).filter(models.User.identification == identification).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# --------------------------------------------------------------------------
# Tutorial
# --------------------------------------------------------------------------
def get_tutorial(db: Session, tutorial_id: int):
    return db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).first()

def get_tutorial_by_name(db: Session, name: str, level: int = None):
    if level:
        return db.query(models.Tutorial).filter(models.Tutorial.name == name and models.Tutorial.level == level).first()
    return db.query(models.Tutorial).filter(models.Tutorial.name == name).first()

def get_tutorials_by_name(db: Session, name: str, level: int = None, skip: int = 0, limit: int = 100):
    if level:
        return db.query(models.Tutorial).filter(models.Tutorial.name == name and models.Tutorial.level == level).offset(skip).limit(limit).all()
    return db.query(models.Tutorial).filter(models.Tutorial.name == name).offset(skip).limit(limit).all()

def get_tutorial_by_topic(db: Session, topic_id: int, level: int = None):
    if level:
        return db.query(models.Tutorial).filter(models.Tutorial.topic_id == topic_id and models.Tutorial.level == level).first()
    return db.query(models.Tutorial).filter(models.Tutorial.topic_id == topic_id).first()

def get_tutorials_by_topic(db: Session, topic_id: int, level: int = None, skip: int = 0, limit: int = 100):
    if level:
        return db.query(models.Tutorial).filter(models.Tutorial.topic_id == topic_id and models.Tutorial.level == level).offset(skip).limit(limit).all()
    return db.query(models.Tutorial).filter(models.Tutorial.topic_id == topic_id).offset(skip).limit(limit).all()
# --------------------------------------------------------------------------
# VIDEO
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Topic
# --------------------------------------------------------------------------
# --------------------------------------------------------------------------
# Vote
# --------------------------------------------------------------------------