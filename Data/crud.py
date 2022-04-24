from sqlalchemy.orm import Session

from . import models, schemas

# --------------------------------------------------------------------------
# User
# --------------------------------------------------------------------------

# GET
def get_user(db: Session, id: int):
    return db.query(models.User).filter(models.User.id == id).first()

def get_user_by_identification(db: Session, identification: str):
    return db.query(models.User).filter(models.User.identification == identification).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
# CREATE
def create_user(db: Session, user: schemas.UserCreate):
    password = user.hashed_password
    db_user = models.User(identification = user.identification, hashed_password = password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
# UPDATE
# DELETE

# --------------------------------------------------------------------------
# Tutorial
# --------------------------------------------------------------------------

# GET
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

def get_tutorials_by_level(db: Session, level: int, skip: int = 0, limit: int = 100):
    return db.query(models.Tutorial).filter(models.Tutorial.level == level).offset(skip).limit(limit).all()

def get_tutorials(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tutorial).offset(skip).limit(limit).all()
# CREATE
def create_tutorial(db: Session, tutorial: schemas.TutorialCreate, user_id: int, topic_id: int):
    db_tutorial =  models.Tutorial(**tutorial.dict(), creator = user_id, topic_id = topic_id)
    db.add(db_tutorial)
    db.commit()
    db.refresh(db_tutorial)
    return db_tutorial

# UPDATE
# DELETE
def delete_tutorial(db: Session, id: int):
    db.query(models.Tutorial).filter(models.Tutorial.id == id).delete()
    db.commit()

# --------------------------------------------------------------------------
# VIDEO
# --------------------------------------------------------------------------

# GET
def get_video(db: Session, video_id: int):
    return db.query(models.Video).filter(models.Video.id == video_id).first()

def get_videos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Video).offset(skip).limit(limit).all()

def get_video_by_name(db: Session, name: str):
    return db.query(models.Video).filter(models.Video.name == name).first()

def get_videos_by_name(db: Session, name: str, skip: int = 0, limit: int = 100):
    return db.query(models.Video).filter(models.Video.name == name).offset(skip).limit(limit).all()

def get_video_by_url(db: Session, url: str):
    return db.query(models.Video).filter(models.Video.url == url).first()
# CREATE
def create_video(db: Session, video: schemas.VideoCreate):
    db_video = models.Video(**video.dict())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video
# UPDATE
# DELETE

# --------------------------------------------------------------------------
# Topic
# --------------------------------------------------------------------------

# GET
def get_topic(db: Session, topic_id: id):
    return db.query(models.Topic).filter(models.Topic.id == topic_id).first()

def get_topics(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).offset(skip).limit(limit).all()

def get_topic_by_name(db: Session, name: str):
    return db.query(models.Topic).filter(models.Topic.name == name).first()

def get_topics_by_name(db: Session, name: str, skip: int = 0, limit: int = 100):
    return db.query(models.Topic).filter(models.Topic.name == name).offset(skip).limit(limit).all()
# CREATE
def create_topic(db: Session, topic: schemas.TopicCreate):
    db_topic = models.Topic(**topic.dict())
    db.add(db_topic)
    db.commit()
    db.refresh(db_topic)
    return db_topic

# UPDATE
# DELETE

# --------------------------------------------------------------------------
# Vote
# --------------------------------------------------------------------------

# GET
def get_vote(db: Session, vote_id: int = 0):
    return db.query(models.Vote).filter(models.Vote.id == vote_id).first()

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
# DELETE