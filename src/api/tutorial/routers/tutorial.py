from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.tutorial.crud import tutorial as crud
from api.tutorial import database, oauth2, schemas

router = APIRouter(
    prefix="/tutorial",
    tags=['Tutorial']
)

@router.post("/", response_model=schemas.Tutorial)
def create_tutorial(tutorial_schema: schemas.TutorialCreate, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return crud.create_tutorial(db, tutorial=tutorial_schema, user_id=current_user.id)

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def delete_tutorial(id: int, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    crud.delete_tutorial(db, tutorial_id=id)

@router.put("/", response_model=schemas.Tutorial , status_code=status.HTTP_202_ACCEPTED)
def update_tutorial(id: int, tutorial_schema: Optional[schemas.TutorialCreate], db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_tutorial = crud.get_tutorial(db, tutorial_id=id)
    crud.update_tutorial(db, tutorial_id=id, tutorial=tutorial_schema)

@router.get("/", response_model=schemas.Tutorial)
def read_tutorial(id: int, db: Session = Depends(database.get_db)):
    db_tutorial = crud.get_tutorial(db, tutorial_id=id)
    if db_tutorial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorial not found")
    return db_tutorial

@router.get("/list/", response_model=List[schemas.Tutorial])
def read_tutorials(skip: Optional[int] = 0, limit: Optional[int] = 100, name: Optional[str] = None,
                   level: Optional[int] = None, topic_id: Optional[int] = None, db: Session = Depends(database.get_db)):
    if name:
        db_tutorials = crud.get_tutorials_by_name(db, name=name,level=level, skip=skip, limit=limit)
    elif topic_id:
        db_tutorials = crud.get_tutorials_by_topic(db, topic_id=topic_id, level=level, skip=skip, limit=limit)
    else:
        db_tutorials = crud.get_tutorials(db, skip=skip, limit=limit)
    if db_tutorials is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorials not found")
    return db_tutorials
