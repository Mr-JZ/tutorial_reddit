from typing import Optional, List

from pydantic import BaseModel


# --------------------------------------------------------------------------
# User
# --------------------------------------------------------------------------
class UserBase(BaseModel):
    identification: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    identification: Optional[str]
    password: Optional[str]

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
# VIDEO
# --------------------------------------------------------------------------
class VideoBase(BaseModel):
    name: str
    url: str

class VideoCreate(VideoBase):
    pass
class VideoUpdate(BaseModel):
    name: Optional[str]
    url: Optional[str]


class Video(VideoBase):
    id: int

    class Config:
        orm_mode = True

class VideoSchema(BaseModel):
    id: int
    name: str
    url: str
    user: Optional[User]

    class Config:
        orm_mode = True
# --------------------------------------------------------------------------
# VIDEO <-> Tutorial
# --------------------------------------------------------------------------
class Videos_TutorialBase(BaseModel):
    video: Optional[VideoSchema]

class Videos_TutorialCreate(Videos_TutorialBase):
    order: int

class Videos_Tutorial(Videos_TutorialBase):
    id: int

    class Config:
        orm_mode = True

class Videos_TutorialSchema(BaseModel):
    id: int
    order: int
    video: Optional[VideoSchema]

    class Config:
        orm_mode = True
# --------------------------------------------------------------------------
# Topic
# --------------------------------------------------------------------------
class TopicBase(BaseModel):
    name: str

class TopicCreate(TopicBase):
    pass

class TopicUpdate(BaseModel):
    name: Optional[str]
class Topic(TopicBase):
    id: int
    user_id : int

    class Config:
        orm_mode =True

class TopicSchema(BaseModel):
    id: int
    name: str
    user: Optional[User]

    class Config:
        orm_mode = True
# --------------------------------------------------------------------------
# Vote
# --------------------------------------------------------------------------
class VoteBase(BaseModel):
    up: bool

class VoteCreate(VoteBase):
    pass

class VoteUpdate(BaseModel):
    up: Optional[bool]
class Vote(VoteBase):
    id: int
    tutorial_id: int
    user_id: int

    class Config:
        orm_mode = True

class VoteSchema(BaseModel):
    id: int
    up: bool
    user: Optional[User]

    class Config:
        orm_mode = True

# --------------------------------------------------------------------------
# Token
# --------------------------------------------------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_identification: str


# --------------------------------------------------------------------------
# Tutorial
# --------------------------------------------------------------------------
class TutorialBase(BaseModel):
    name: str
    level: int
    topic_id: int


class TutorialCreate(TutorialBase):
    description: str | None = None


class TutorialUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    level: Optional[int]
    topic_id: Optional[int]



class Tutorial(TutorialBase):
    id: int
    creator: int

    class Config:
        orm_mode = True

class TutorialSchema(BaseModel):
    id: int
    name: str
    description: str | None = None
    topic: TopicSchema
    level: int
    votes: List[VoteSchema]
    videos: List[Videos_TutorialSchema]
    user: User

    class Config:
        orm_mode = True



