from fastapi import FastAPI
from tutorial import  models
from tutorial.database import engine
from tutorial.routers import tutorial, user, authentication, video, vote, topic

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(tutorial.router)
app.include_router(vote.router)
app.include_router(video.router)
app.include_router(topic.router)
