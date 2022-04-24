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
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/user/", response_model=schemas.User)
def read_user(user_id: Optional[int] = None, identification: Optional[str] = None, db: Session = Depends(get_db)):
    if user_id:
        db_user = crud.get_user(db, id=user_id)
    elif identification:
        db_user = crud.get_user_by_identification(db, identification=identification)
    else:
        raise HTTPException(status_code=404, detail="No input provided")
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
# --------------------------------------------------------------------------
# Tutorial
# --------------------------------------------------------------------------
@app.post("/tutorial/", response_model=schemas.Topic)
def create_tutorial(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    pass

@app.get("/tutorial/", response_model=schemas.Topic)
def read_tutorial(topic_id: int, db: Session = Depends(get_db)):
    pass

@app.get("/tutorials/", response_model=schemas.Topic)
def read_tutorials(skip: int, limit: int, db: Session = Depends(get_db)):
    pass
# --------------------------------------------------------------------------
# VIDEO
# --------------------------------------------------------------------------
@app.post("/video/", response_model=schemas.Topic)
def create_video(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    pass

@app.get("/video/", response_model=schemas.Topic)
def read_video(topic_id: int, db: Session = Depends(get_db)):
    pass

@app.get("/videos/", response_model=schemas.Topic)
def read_videos(skip: int, limit: int, db: Session = Depends(get_db)):
    pass
# --------------------------------------------------------------------------
# Topic
# --------------------------------------------------------------------------
@app.post("/topic/", response_model=schemas.Topic)
def create_topic(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    pass

@app.get("/topic/", response_model=schemas.Topic)
def read_topic(topic_id: int, db: Session = Depends(get_db)):
    pass

@app.get("/topics/", response_model=schemas.Topic)
def read_topics(skip: int, limit: int, db: Session = Depends(get_db)):
    pass
# --------------------------------------------------------------------------
# Vote
# --------------------------------------------------------------------------
@app.post("/vote/", response_model=schemas.Topic)
def create_vote(topic: schemas.TopicCreate, db: Session = Depends(get_db)):
    pass

@app.get("/vote/", response_model=schemas.Topic)
def read_vote(topic_id: int, db: Session = Depends(get_db)):
    pass

@app.get("/votes/", response_model=schemas.Topic)
def read_votes(skip: int, limit: int, db: Session = Depends(get_db)):
    pass
