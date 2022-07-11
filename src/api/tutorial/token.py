from datetime import datetime, timedelta
from jose import JWTError, jwt
from src.api.tutorial import schemas
import src.api.tutorial.crud.user as user
from sqlalchemy.orm import Session
import json
import os


with open(os.path.join(os.getenv("SECRETE"), "tutorial_reddit_secret.json")) as file:
    security = json.load(file)


# to get a string like this run:
# openssl rand -hex 32 and put it into the secret.json file
SECRET_KEY = security.get("secret_key")
ALGORITHM = security.get("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = security.get("acces_token_expire_minutes")

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(db: Session, token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        identification: str = payload.get("sub")
        if identification is None:
            raise credentials_exception
        token_data = schemas.TokenData(user_identification=identification)
    except JWTError:
        raise credentials_exception
    db_user = user.get_user_by_identification(db, identification=token_data.user_identification)
    if db_user is None:
        raise credentials_exception
    return db_user