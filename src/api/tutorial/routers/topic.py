from typing import Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.api.tutorial.crud import topic
from src.api.tutorial import database, oauth2, schemas
from src.api.tutorial.user_role import Role

router = APIRouter(
    prefix="/topic",
    tags=['Topic']
)

@router.post("/", response_model=schemas.Topic)
def create_topic(topic_schema: schemas.TopicCreate, db: Session = Depends(database.get_db),
                 current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_topic = topic.get_topic_by_name(db, name=topic_schema.name)
    if db_topic:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Topic already exist")
    return topic.create_topic(db, topic=topic_schema, user_id=current_user.id)

@router.get("/", response_model=schemas.Topic)
def read_topic(id: Optional[int] = None, name: Optional[str] = None, db: Session = Depends(database.get_db)):
    if id is not None:
        db_topic = topic.get_topic(db, topic_id=id)
    elif name is not None:
        db_topic = topic.get_topic_by_name(db, name=name)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No inputs")
    if db_topic is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This topic don't exist")
    return db_topic


@router.get("/list/", response_model=schemas.Topic)
def read_topics(skip: int, limit: int, db: Session = Depends(database.get_db)):
    db_topics = topic.get_topics(db, skip=skip, limit=limit)
    if db_topics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This topics don't exist")
    return db_topics

@router.delete("/")
def delete_topic(topic_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(
    oauth2.get_current_user)):
    topic_db = topic.get_topic(db, topic_id=topic_id)
    if topic_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This topic don't exist")
    elif topic_db.user_id == current_user.id or current_user.acces_level == Role().ADMIN:
        topic.delete_topic(db, topic_id=topic_id)

@router.put("/")
def update_topic(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # TODO: add update topic
    pass