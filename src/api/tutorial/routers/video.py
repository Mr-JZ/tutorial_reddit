from typing import Optional, List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.tutorial.crud import video as crud
from api.tutorial import database, oauth2, schemas, models
from api.tutorial.user_role import Role

router = APIRouter(
    prefix="/video",
    tags=['Video']
)

@router.post("", response_model=schemas.VideoSchema)
def create_video(video: schemas.VideoCreate, db: Session = Depends(database.get_db),
                 current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_video = crud.get_video_by_url(db, url=video.url)
    if db_video:
        return schemas.VideoSchema.from_orm(db_video)
    return schemas.VideoSchema.from_orm(crud.create_video(db, video=video))

@router.get("", response_model=schemas.VideoSchema)
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
    return schemas.VideoSchema.from_orm(db_video)


@router.get("/list", response_model=List[schemas.VideoSchema])
def read_videos(skip: Optional[int] = 0, limit: Optional[int] = 100, name: Optional[str] = None, db: Session = Depends(
    database.get_db)):
    videos: List[schemas.VideoSchema] = []
    if name:
        db_videos = crud.get_videos_by_name(db, name=name, skip=skip, limit=limit)
    else:
        db_videos = crud.get_videos(db, skip=skip, limit=limit)
    if db_videos is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Videos not found")
    else:
        for video in db_videos:
            videos.append(schemas.VideoSchema.from_orm(video))
    return videos

@router.delete("")
def delete_video(video_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(
    oauth2.get_current_user)):
    db_video = crud.get_video(db, video_id=video_id)
    if db_video is None:
        pass
    elif current_user.acces_level >= Role().MODERATOR:
        crud.delete_video(db, db_video.id)

@router.put("", response_model=schemas.VideoSchema)
def update_video(id: int, video: schemas.VideoUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_video = db.get(models.Video, id)
    if not db_video:
        raise HTTPException(status_code=404, detail="Video not found")
    if db_video.user_id == current_user.id:
        video_data = video.dict(exclude_unset=True)
        for key, value in video_data.items():
            setattr(db_video, key, value)
        db.add(db_video)
        db.commit()
        db.refresh(db_video)
    return schemas.VideoSchema.from_orm(db_video)
