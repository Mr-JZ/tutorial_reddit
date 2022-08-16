from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.tutorial.crud import tutorial as crud
from api.tutorial import database, oauth2, schemas, models

router = APIRouter(
    prefix="/tutorial",
    tags=['Tutorial']
)

@router.post("", response_model=schemas.TutorialSchema)
def create_tutorial(tutorial_schema: schemas.TutorialCreate, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return schemas.TutorialSchema.from_orm(crud.create_tutorial(db, tutorial=tutorial_schema, user_id=current_user.id))

@router.post("/{tutorial_id}/video")
def add_tutorial_video(id: int, tutorial_id: int, order: int, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return crud.add_video(db, tutorial_id=tutorial_id, Tutorial=id, order=order)

@router.put("/{tutorial_id}/video")
def update_tutorial_video(id: int, tutorial_id: int, order: int, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    return crud.update_video_order(db, tutorial_id=tutorial_id, Tutorial=id, order=order)


@router.get("/{tutorial_id}/video")
def get_tutorial_videos(tutorial_id: int, skip: int, limit: int, db: Session = Depends(database.get_db)):
    return crud.get_videos(db, tutorial_id=tutorial_id)

@router.delete("/{tutorial_id}/video", status_code=status.HTTP_204_NO_CONTENT)
def delete_tutorial_videos(id: int, tutorial_id: int, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    crud.delete_video(db, tutorial_id=tutorial_id, Tutorial=id)

@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
def delete_tutorial(id: int, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    crud.delete_tutorial(db, tutorial_id=id)

@router.put("", response_model=schemas.TutorialSchema , status_code=status.HTTP_202_ACCEPTED)
def update_tutorial(id: int, tutorial: schemas.TutorialUpdate, db: Session = Depends(database.get_db),
                    current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_tutorial = db.get(models.Tutorial, id)
    if not db_tutorial:
        raise HTTPException(status_code=404, detail="Vote not found")
    if db_tutorial.user_id == current_user.id:
        tutorial_data = tutorial.dict(exclude_unset=True)
        for key, value in tutorial_data.items():
            setattr(db_tutorial, key, value)
        db.add(db_tutorial)
        db.commit()
        db.refresh(db_tutorial)
    return schemas.TutorialSchema.from_orm(db_tutorial)


@router.get("", response_model=schemas.TutorialSchema)
def get_tutorial(id: int, db: Session = Depends(database.get_db)):
    db_tutorial = crud.get_tutorial(db, tutorial_id=id)
    if db_tutorial is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorial not found")
    return schemas.TutorialSchema.from_orm(db_tutorial)

@router.get("/list", response_model=List[schemas.TutorialSchema])
def get_tutorials(skip: Optional[int] = 0, limit: Optional[int] = 100, name: Optional[str] = None,
                  level: Optional[int] = None, topic_id: Optional[int] = None, db: Session = Depends(database.get_db),
                  ):
    tutorials : List[schemas.TutorialSchema] = []
    db_tutorials = crud.get_tutorials(db, name=name, topic_id=topic_id, level=level, skip=skip, limit=limit)
    if db_tutorials is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tutorials not found")
    else:
        for tutorial in db_tutorials:
            tutorials.append(schemas.TutorialSchema.from_orm(tutorial))
    return tutorials
