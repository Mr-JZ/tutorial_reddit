from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from src.api.tutorial import token
from src.api.tutorial.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(db: Session = Depends(get_db), data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token.verify_token(db, data, credentials_exception)
