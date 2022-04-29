from sqlalchemy.orm import Session
from typing import Optional
from .. import models, schemas

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

