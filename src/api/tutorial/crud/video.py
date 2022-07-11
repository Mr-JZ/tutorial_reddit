from sqlalchemy.orm import Session
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
def update_video(db: Session, video_id: int, video: schemas.VideoCreate):
    db_video = get_video(db, video_id=video_id)
    if video.name:
        db_video.name = video.name
    if video.url:
        db_video.url = video.url
    db.commit()
    db.refresh(db_video)
    return db_video

# DELETE
def delete_video(db: Session, video_id: int):
    db.query(models.Video).filter(models.Video.id == id).delete()
    db.commit()

