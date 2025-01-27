from datetime import datetime, timedelta
from jose import JWTError, jwt
from src.api.tutorial import schemas
import src.api.tutorial.crud.user as user
from sqlalchemy.orm import Session
import json
import os


# Load and validate configuration
try:
    security = json.loads(os.getenv("TUTORIAL_REDDIT_SECRET", "{}"))
except json.JSONDecodeError:
    raise RuntimeError("Invalid JSON in TUTORIAL_REDDIT_SECRET environment variable")

# to get a string like this run:
# openssl rand -hex 32 and put it into the secret.json file
SECRET_KEY = security.get("SECRET_KEY")
ALGORITHM = security.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(security.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Validate required configuration
if not all([SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES]):
    raise RuntimeError(
        "Missing required configuration in TUTORIAL_REDDIT_SECRET. Required keys: SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES"
    )


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
    db_user = user.get_user_by_identification(
        db, identification=token_data.user_identification
    )
    if db_user is None:
        raise credentials_exception
    return db_user
