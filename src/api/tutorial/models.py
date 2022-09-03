from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Video(Base):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    tutorials = relationship("Videos_Tutorial", back_populates="video")
    user = relationship("User", back_populates="video")

class Videos_Tutorial(Base):
    __tablename__ = "videos_tutorial"
    id = Column(Integer, primary_key=True, index=True)

    order = Column(Integer)
    video_id = Column(Integer, ForeignKey("video.id"))
    tutorial_id = Column(Integer, ForeignKey("tutorial.id"))

    tutorial = relationship("Tutorial", back_populates="videos")
    video = relationship("Video", back_populates="tutorials")

class Tutorial(Base):
    __tablename__ = "tutorial"
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    description = Column(String, index=True)
    topic_id = Column(Integer, ForeignKey("topic.id"))
    level = Column(Integer, index=True)
    # the creator
    creator = Column(Integer, ForeignKey("user.id"))

    videos = relationship("Videos_Tutorial", back_populates="tutorial")
    topic = relationship("Topic", back_populates="tutorial")
    user = relationship("User", back_populates="tutorial")
    votes = relationship("Vote", back_populates="tutorial")

class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    name = Column(String, unique=True, index=True)

    tutorial = relationship("Tutorial", back_populates="topic")
    user = relationship("User", back_populates="topic")

class Vote(Base):
    __tablename__ = "vote"
    id = Column(Integer, primary_key=True, index=True)

    tutorial_id = Column(Integer, ForeignKey("tutorial.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    up = Column(Boolean)

    tutorial = relationship("Tutorial", back_populates="votes")
    user = relationship("User", back_populates="vote")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)

    identification = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    access_level = Column(Integer, default=0)

    vote = relationship("Vote", back_populates="user")
    tutorial = relationship("Tutorial", back_populates="user")
    video = relationship("Video", back_populates="user")
    topic = relationship("Topic", back_populates="user")
