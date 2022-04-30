from typing import Optional
from pydantic import BaseModel

# --------------------------------------------------------------------------
# VIDEO
# --------------------------------------------------------------------------
class VideoBase(BaseModel):
    name: str
    url: str

class VideoCreate(VideoBase):
    pass

class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True

# --------------------------------------------------------------------------
# Tutorial
# --------------------------------------------------------------------------
class TutorialBase(BaseModel):
    name: str
    level: int
    topic_id: int

class TutorialCreate(TutorialBase):
    description: str | None = None

class Tutorial(TutorialBase):
    id: int
    creator: int
    user_id : int

    class Confi:
        orm_mode = True
# --------------------------------------------------------------------------
# VIDEO <-> Tutorial
# --------------------------------------------------------------------------
class Video_TutorialBase(BaseModel):
    video_id: int
    tutorial_id: int

class Video_TutorialCreate(Video_TutorialBase):
    order: int

class Video_Tutorial(Video_TutorialBase):
    id: int

    class Config:
        orm_mode = True
# --------------------------------------------------------------------------
# Topic
# --------------------------------------------------------------------------
class TopicBase(BaseModel):
    name: str

class TopicCreate(TopicBase):
    pass

class Topic(TopicBase):
    id: int
    user_id : int

    class Config:
        orm_mode =True
# --------------------------------------------------------------------------
# Vote
# --------------------------------------------------------------------------
class VoteBase(BaseModel):
    up: bool

class VoteCreate(VoteBase):
    pass

class Vote(VoteBase):
    id: int
    tutorial_id: int
    user_id: int

    class Config:
        orm_mode = True
# --------------------------------------------------------------------------
# User
# --------------------------------------------------------------------------
class UserBase(BaseModel):
    identification: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    acces_level: Optional[int] = 0

    class Config:
        orm_mode = True

class UserShow(UserBase):
    is_active: bool
    acces_level: Optional[int] = 0

# --------------------------------------------------------------------------
# Token
# --------------------------------------------------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_identification: str
