from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from tutorial.crud import user
from tutorial import schemas, models, oauth2, crud, database
from tutorial.user_role import Role

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

@router.get("/list/", response_model=List[schemas.User])
def read_users(skip: Optional[int] = 0, limit: Optional[int] = 100, db: Session = Depends(database.get_db)):
    users = user.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/", response_model=schemas.User)
def read_user(id: Optional[int] = None, identification: Optional[str] = None, db: Session = Depends(database.get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    if id:
        db_user = user.get_user(db, id=id)
    elif identification:
        db_user = user.get_user_by_identification(db, identification=identification)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No input provided")
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.delete("/")
def delete_user(user_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_user = user.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The User doesn't exist")
    elif db_user.id == current_user.id or current_user.acces_level == Role().ADMIN:
        user.delete_user(db, user_id=user_id)

@router.put("/")
def update_user(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    # TODO: add update function
    pass
