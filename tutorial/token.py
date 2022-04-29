from datetime import datetime, timedelta
from jose import JWTError, jwt
from tutorial import schemas
import tutorial.crud.user as user
from sqlalchemy.orm import Session

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "0d93fb65c44b928773737e903db351aa169e7b7963f93ffe0f84534487fdc3c365c607d1f91b1da1d29523b7a547b77e194f0bf715ba309087339cd4efb32270"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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