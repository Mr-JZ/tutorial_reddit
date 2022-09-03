from sqlalchemy.orm import Session, joinedload
from typing import Optional
from api.tutorial import models, schemas

# GET
def get_tutorial(db: Session, tutorial_id: int):
    return db.query(models.Tutorial)\
        .filter(models.Tutorial.id == tutorial_id).first()

def get_tutorials_by_name(db: Session, name: str, level: int = None, skip: int = 0, limit: int = 100):
    if level:
        return db.query(models.Tutorial).filter(
            models.Tutorial.name == name and models.Tutorial.level == level).offset(skip).limit(limit).all()
    return db.query(models.Tutorial).filter(models.Tutorial.name == name).offset(skip).limit(limit).all()

def get_tutorials_by_topic(db: Session, topic_id: int, level: int = None, skip: int = 0, limit: int = 100):
    if level:
        return db.query(models.Tutorial).filter(
            models.Tutorial.topic_id == topic_id and models.Tutorial.level == level).offset(skip).limit(limit).all()
    return db.query(models.Tutorial).filter(models.Tutorial.topic_id == topic_id).offset(skip).limit(limit).all()

def get_tutorials(db: Session, name: str = None, topic_id: int = None, level: int = None, skip: int = 0, limit: int = 100):
    nameBool = False
    topicBool = False
    levelBool = False
    if name is None:
        nameBool = True
        name = ""
    if topic_id is None:
        topicBool = True
        topic_id = 0
    if level is None:
        levelBool = True
        level = 0
    print(f"INFO: tutorial.get_tutorials - name = {name}:{nameBool}; topic = {topic_id}:{topicBool}; levelBool = {level}:{levelBool}")
    return db.query(models.Tutorial).filter(
        (models.Tutorial.name == name or nameBool) and
        (models.Tutorial.topic_id == topic_id or topicBool) and
        (models.Tutorial.level == level or levelBool)).offset(skip).limit(limit).all()

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
    db.query(models.Tutorial).filter(models.Tutorial.id == tutorial_id).delete()
    db.commit()

# Video adding
def add_video(db: Session, tutrial_id: int, video_id: int, order: int):
    db_video_tutorial = models.Videos_Tutorial(video_id=video_id, tutrial_id=tutrial_id, order=order)
    db.add(db_video_tutorial)
    db.commit()
    db.refresh(db_video_tutorial)
    return db_video_tutorial

def update_video_order(db: Session, tutorial_id: int, video_id: int, order):
    db_video_tutorial = get_video_tutorial(db, tutorial_id=tutorial_id, video_id=video_id)
    db_video_tutorial.order = order
    db.commit()
    db.refresh(db_video_tutorial)
    return db_video_tutorial

def get_videos(db: Session, tutorial_id: int, skip: int, limit: int):
    return db.query(models.Videos_Tutorial).filter(
        models.Videos_Tutorial.tutorial_id == tutorial_id).offset(skip).limit(limit).all()

def delete_video(db: Session, tutorial_id: int, video_id: int):
    db.query(models.Videos_Tutorial).filter(models.Videos_Tutorial.video_id == video_id and models.Videos_Tutorial.tutorial_id == tutorial_id).delete(synchronize_session=False)
    db.commit()

def get_video_tutorial(db: Session, tutorial_id: int, video_id: int):
    return db.query(models.Videos_Tutorial).filter(models.Videos_Tutorial.tutorial_id == tutorial_id and
                                                   models.Videos_Tutorial.video_id == video_id).first()