from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from tutorial.crud import user
from tutorial import schemas, models, oauth2, crud, database

router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.post("/", response_model=schemas.User)
def create_user(user_schema: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = user.get_user_by_identification(db, identification=user_schema.identification)
    if db_user:
        raise HTTPException(status_code=400, detail="Identification already exist")
    return user.create_user(db=db, user=user_schema)

@router.get("/", response_model=list[schemas.User])
def read_users(skip: Optional[int] = 0, limit: Optional[int] = 100, db: Session = Depends(database.get_db)):
    users = user.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/", response_model=schemas.User)
def read_user(id: Optional[int] = None, identification: Optional[str] = None, db: Session = Depends(database.get_db)):
    if id:
        db_user = user.get_user(db, id=id)
    elif identification:
        db_user = user.get_user_by_identification(db, identification=identification)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No input provided")
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
