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
    level: str
    creator: int

class TutorialCreate(TutorialBase):
    pass

class Tutorial(TutorialBase):
    description: str | None = None
    id: int
    topic_id: int

    class Confi:
        orm_mode = True
# --------------------------------------------------------------------------
# VIDEO <-> Tutorial
# --------------------------------------------------------------------------
class Video_TutorialBase(BaseModel):
    pass

class Video_TutorialCreate(Video_TutorialBase):
    pass

class Video_Tutorial(Video_TutorialBase):
    id: int
    video_id: int
    tutorial_id: int

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
    acces_level: int

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
