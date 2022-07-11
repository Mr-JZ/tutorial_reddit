from fastapi import FastAPI
from src.api.tutorial import  models
from src.api.tutorial import engine
from mangum import Mangum
from src.api.tutorial import tutorial, user, authentication, vote
from src.api.tutorial.routers import video, topic, web_tutorial

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(web_tutorial.router)
app.include_router(user.router)
app.include_router(tutorial.router)
app.include_router(vote.router)
app.include_router(video.router)
app.include_router(topic.router)

handler = Mangum(app=app)