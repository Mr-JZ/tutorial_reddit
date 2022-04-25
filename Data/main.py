from typing import Optional
from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session
from . import schemas, models, database, crud

app = FastAPI()

models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------------------------------------------------------------
# User
# --------------------------------------------------------------------------

@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_identification(db, identification=user.identification)
    if db_user:
        raise HTTPException(status_code=400, detail="Identification already exist")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: Optional[int] = 0, limit: Optional[int] = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/", response_model=schemas.User)
def read_user(user_id: Optional[int] = None, identification: Optional[str] = None, db: Session = Depends(get_db)):
    if user_id:
        db_user = crud.get_user(db, id=user_id)
    elif identification:
        db_user = crud.get_user_by_identification(db, identification=identification)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No input provided")
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
# --------------------------------------------------------------------------
# Tutorial
# --------------------------------------------------------------------------
@app.post("/tutorial/", response_model=schemas.Tutorial)
def create_tutorial(tutorial: schemas.TutorialCreate, db: Session = Depends(get_db)):
    return crud.create_tutorial(db, tutorial=tutorial)

@app.get("/tutorial/", response_model=schemas.Tutorial)
def read_tutorial(tutorial_id: int, db: Session = Depends(get_db)):
    db_tutorial = crud.get_tutorial(db, tutorial_id=tutorial_id)
    if db_tutorial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorial not found")
    return db_tutorial

@app.get("/tutorials/", response_model=list(schemas.Tutorial))
def read_tutorials(skip: Optional[int] = 0, limit: Optional[int] = 100, name: Optional[str] = None,
                   level: Optional[int] = None, topic_id: Optional[int] = None, db: Session = Depends(get_db)):
    if name:
        db_tutorials = crud.get_topics_by_name(db, name=name,level=level, skip=skip, limit=limit)
    elif topic_id:
        db_tutorials = crud.get_tutorials_by_topic(db, topic_id=topic_id, level=level, skip=skip, limit=limit)
    else:
        db_tutorials = crud.get_topics(db, skip=skip, limit=limit)
    if db_tutorials is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorials not found")
    return db_tutorials
# --------------------------------------------------------------------------
# VIDEO
# --------------------------------------------------------------------------
@app.post("/video/", response_model=schemas.Video)
def create_video(video: schemas.VideoCreate, db: Session = Depends(get_db)):
    db_video = crud.get_video_by_url(db, url=video.url)
    if db_video:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Video exist already")
    return crud.create_video(db, video=video)

@app.get("/video/", response_model=schemas.Video)
def read_video(video_id: Optional[int] = None, url: Optional[str] = None, name: Optional[str] = None, db: Session = Depends(get_db)):
    if video_id:
        db_video = crud.get_video(db, video_id=video_id)
    elif url:
        db_video = crud.get_video_by_url(db, url=url)
    elif name:
        db_video = crud.get_video_by_name(db, name=name)
    else:
        pass
    if db_video is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Video not found")
    return db_video


@app.get("/videos/", response_model=list(schemas.Video))
def read_videos(skip: Optional[int] = 0, limit: Optional[int] = 100, name: Optional[str] = None, db: Session = Depends(get_db)):
    if name:
        db_videos = crud.get_videos_by_name(db, name=name, skip=skip, limit=limit)
    else:
        db_videos = crud.get_videos(db, skip=skip, limit=limit)
    if db_videos is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Videos not found")
    return db_videos

# --------------------------------------------------------------------------
# Topic
# --------------------------------------------------------------------------
@app.post("/topic/", response_model=schemas.Topic)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    db_topic = crud.get_topic_by_name(db, name=topic.name)
    if db_topic:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Topic already exist")
    return crud.create_topic(db, topic=topic)

@app.get("/topic/", response_model=schemas.Topic)
def read_topic(topic_id: Optional[int] = None,name: Optional[str] = None, db: Session = Depends(get_db)):
    if topic_id:
        db_topic = crud.get_topic(db, topic_id=topic_id)
    elif name:
        db_topic = crud.get_topic_by_name(db, name=name)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No inputs")
    if db_topic is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This topic don't exist")
    return db_topic


@app.get("/topics/", response_model=list(schemas.Topic))
def read_topics(skip: int, limit: int, db: Session = Depends(get_db)):
    db_topics = crud.get_topics(db, skip=skip, limit=limit)
    if db_topics is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This topics don't exist")
    return db_topics
# --------------------------------------------------------------------------
# Vote
# --------------------------------------------------------------------------
@app.post("/vote/", response_model=schemas.Vote)
def create_vote(vote: schemas.VoteCreate, user_id: int, tutorial_id: int, db: Session = Depends(get_db)):
    db_vote = crud.get_vote_by_user_and_tutorial_id(db, user_id=user_id, tutorial_id=tutorial_id)
    if db_vote:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vote already exists")
    return crud.create_vote(db, vote=vote, user_id=user_id, tutorial_id=tutorial_id)

@app.get("/vote/", response_model=schemas.Vote)
def read_vote(vote_id: Optional[int], tutorial_id: Optional[int], user_id: Optional[int], db: Session = Depends(get_db)):
    if vote_id:
        db_vote = crud.get_vote(db, vote_id=vote_id)
    elif tutorial_id and user_id:
        db_vote = crud.get_vote_by_user_and_tutorial_id(db, user_id=user_id, tutorial_id=tutorial_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No inputs")
    if db_vote is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No element found")
    return db_vote

@app.get("/votes/", response_model=list(schemas.Vote))
def read_votes(skip: Optional[int] = 0, limit: Optional[int] = 100, user_id: Optional[int] = None,
               tutorial_id: Optional[int] = None, db: Session = Depends(get_db)):
    if user_id:
        db_votes = crud.get_votes_by_user(db, user_id=user_id, skip=skip, limit=limit)
    elif tutorial_id:
        db_votes = crud.get_votes_by_tutorial(db, tutorial_id=tutorial_id, skip=skip, limit=limit)
    else:
        db_votes = crud.get_votes(db, skip=skip, limit=limit)
    if db_votes is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No return from database")
    return db_votes
