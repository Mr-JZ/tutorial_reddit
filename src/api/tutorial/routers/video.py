from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.tutorial.crud import video as crud
from api.tutorial import database, oauth2, schemas
from api.tutorial.user_role import Role

router = APIRouter(
    prefix="/video",
    tags=['Video']
)

@router.post("", response_model=schemas.Video)
def create_video(video: schemas.VideoCreate, db: Session = Depends(database.get_db),
                 current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_video = crud.get_video_by_url(db, url=video.url)
    if db_video:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Video exist already")
    return crud.create_video(db, video=video)

@router.get("", response_model=schemas.Video)
def read_video(id: Optional[int] = None, url: Optional[str] = None, name: Optional[str] = None, db: Session = Depends(
    database.get_db)):
    if id:
        db_video = crud.get_video(db, video_id=id)
    elif url:
        db_video = crud.get_video_by_url(db, url=url)
    elif name:
        db_video = crud.get_video_by_name(db, name=name)
    if db_video is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The video doesn't exist")
    return db_video


@router.get("/list", response_model=schemas.Video)
def read_videos(skip: Optional[int] = 0, limit: Optional[int] = 100, name: Optional[str] = None, db: Session = Depends(
    database.get_db)):
    if name:
        db_videos = crud.get_videos_by_name(db, name=name, skip=skip, limit=limit)
    else:
        db_videos = crud.get_videos(db, skip=skip, limit=limit)
    if db_videos is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Videos not found")
    return db_videos

@router.delete("")
def delete_video(video_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(
    oauth2.get_current_user)):
    db_video = crud.get_video(db, video_id=video_id)
    if db_video is None:
        pass
    elif current_user.acces_level >= Role().MODERATOR:
        crud.delete_video(db, db_video.id)

@router.put("")
def update_video(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # TODO: add update function
    pass