from typing import Optional, List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from api.tutorial.crud import vote as crud
from api.tutorial import database, oauth2, schemas, models
from api.tutorial.user_role import Role

tutorial_id: int = 0

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("", response_model=schemas.VoteSchema)
def create_vote(vote: schemas.VoteCreate, tutorial_id: int, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
    db_vote = crud.get_vote_by_user_and_tutorial_id(db, user_id=current_user.id, tutorial_id=tutorial_id)
    if db_vote:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vote already exists")
    return schemas.VoteSchema.from_orm(crud.create_vote(db, vote=vote, user_id=current_user.id, tutorial_id=tutorial_id))

@router.get("", response_model=schemas.VoteSchema)
def read_vote(id: Optional[int], db: Session = Depends(database.get_db)):
    db_vote = crud.get_vote(db, vote_id=id)
    if db_vote is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No element found")
    return schemas.VoteSchema.from_orm(db_vote)

@router.get("/list", response_model=List[schemas.VoteSchema])
def read_votes(skip: Optional[int] = 0, limit: Optional[int] = 100,
               tutorial_id: Optional[int] = None, db: Session = Depends(database.get_db)):
    votes: List[schemas.VoteSchema] = []
    if tutorial_id:
        db_votes = crud.get_votes_by_tutorial(db, tutorial_id=tutorial_id, skip=skip, limit=limit)
    else:
        db_votes = crud.get_votes(db, skip=skip, limit=limit)
    if db_votes is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No return from database")
    else:
        for vote in db_votes:
            votes.append(schemas.VoteSchema.from_orm(vote))
    return votes

@router.get("/login", response_model=schemas.VoteSchema)
def read_vote(id: Optional[int], tutorial_id: Optional[int],
              db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    if id:
        db_vote = crud.get_vote(db, vote_id=id)
    elif tutorial_id:
        db_vote = crud.get_vote_by_user_and_tutorial_id(db, user_id=current_user.id, tutorial_id=tutorial_id)
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No inputs")
    if db_vote is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No element found")
    return schemas.VoteSchema.from_orm(db_vote)

@router.get("/login/list", response_model=List[schemas.VoteSchema])
def read_votes(skip: Optional[int] = 0, limit: Optional[int] = 100, user_id: Optional[bool] = False,
               tutorial_id: Optional[int] = None, db: Session = Depends(database.get_db),
               current_user: schemas.User = Depends(oauth2.get_current_user)):
    votes: List[schemas.VoteSchema] = []
    if user_id:
        db_votes = crud.get_votes_by_user(db, user_id=current_user.id, skip=skip, limit=limit)
    elif tutorial_id:
        db_votes = crud.get_votes_by_tutorial(db, tutorial_id=tutorial_id, skip=skip, limit=limit)
    else:
        db_votes = crud.get_votes(db, skip=skip, limit=limit)
    if db_votes is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No return from database")
    else:
        for vote in db_votes:
            votes.append(schemas.VoteSchema.from_orm(vote))
    return votes

@router.delete("")
def delete_vote(vote_id: int, db: Session = Depends(database.get_db), current_user: schemas.User = Depends(
    oauth2.get_current_user)):
    db_vote = crud.get_vote(db, vote_id=vote_id)
    if db_vote is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The vote doesn't exist")
    elif db_vote.user_id == current_user.id or current_user.acces_level == Role().ADMIN:
        crud.delete_vote(db, vote_id=vote_id)


@router.put("", response_model=schemas.VoteSchema)
def update_vote(id :int, vote: schemas.VoteUpdate, db: Session = Depends(database.get_db),
                current_user: schemas.User = Depends(oauth2.get_current_user)):
        db_vote = db.get(models.Vote, id)
        if not db_vote:
            raise HTTPException(status_code=404, detail="Vote not found")
        if db_vote.user_id == current_user.id:
            vote_data = vote.dict(exclude_unset=True)
            for key, value in vote_data.items():
                setattr(db_vote, key, value)
            db.add(db_vote)
            db.commit()
            db.refresh(db_vote)
        return schemas.VoteSchema.from_orm(db_vote)