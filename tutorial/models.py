from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Video(Base):
    __tablename__ = 'video'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    relation = relationship("Videos_Tutorial", back_populates="video")
    user = relationship("User", back_populates="video_relation")

class Videos_Tutorial(Base):
    __tablename__ = "videos_tutorial"
    id = Column(Integer, primary_key=True, index=True)

    video_id = Column(Integer, ForeignKey("video.id"))
    tutorial_id = Column(Integer, ForeignKey("tutorial.id"))

    video = relationship("Video", back_populates="relation")
    tutorial = relationship("Tutorial", back_populates="video_relation")

class Tutorial(Base):
    __tablename__ = "tutorial"
    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, index=True)
    description = Column(String, index=True)
    topic_id = Column(Integer, ForeignKey("topic.id"))
    level = Column(Integer, index=True)
    # the creator
    creator = Column(Integer, ForeignKey("user.id"))

    video_relation = relationship("Videos_Tutorial", back_populates="tutorial")
    topic_relation = relationship("Topic", back_populates="tutorial")
    user_relation = relationship("User", back_populates="tutorial")
    vote_relation = relationship("Vote", back_populates="tutorial")

class Topic(Base):
    __tablename__ = "topic"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))

    name = Column(String, unique=True, index=True)

    tutorial = relationship("Tutorial", back_populates="topic_relation")
    user = relationship("User", back_populates="topic_relation")

class Vote(Base):
    __tablename__ = "vote"
    id = Column(Integer, primary_key=True, index=True)

    tutorial_id = Column(Integer, ForeignKey("tutorial.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    up = Column(Boolean)

    tutorial = relationship("Tutorial", back_populates="vote_relation")
    user = relationship("User", back_populates="vote")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)

    identification = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    access_level = Column(Integer, default=0)

    vote = relationship("Vote", back_populates="user")
    tutorial = relationship("Tutorial", back_populates="user_relation")
    video_relation = relationship("Video", back_populates="user")
    topic_relation = relationship("Topic", back_populates="user")
