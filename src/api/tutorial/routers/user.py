from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.tutorial.crud import user
from api.tutorial import database, oauth2, schemas, models
from api.tutorial.user_role import Role
from api.tutorial.hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=['User']
)

@router.post("", response_model=schemas.User)
def create_user(user_schema: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = user.get_user_by_identification(db, identification=user_schema.identification)
    if db_user:
        raise HTTPException(status_code=400, detail="Identification already exist")
    return user.create_user(db=db, user=user_schema)

@router.get("/list", response_model=List[schemas.User])
def read_users(skip: Optional[int] = 0, limit: Optional[int] = 100, db: Session = Depends(database.get_db)):
    users = user.get_users(db, skip=skip, limit=limit)
    return users

@router.get("", response_model=schemas.User)
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

@router.delete("")
def delete_user(user_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(
    oauth2.get_current_user)):
    db_user = user.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The User doesn't exist")
    elif db_user.id == current_user.id or current_user.acces_level == Role().ADMIN:
        return user.delete_user(db, user_id=user_id)

@router.put("")
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_user = db.get(models.User, id)
    if not db_user:
        raise HTTPException(status_code=404, detail="Vote not found")
    if db_user.id == current_user.id:
        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            if key == "password":
                value = Hash.bcrypt(value)
            setattr(db_user, key, value)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user
