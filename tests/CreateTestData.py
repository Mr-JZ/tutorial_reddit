from api.tutorial.crud import topic, tutorial, user, video, vote
from api.tutorial import database, schemas

db = database.get_db()


# create a user
_user = user.get_user(db=db, id=1)

# create a topic
testTopic = schemas.TopicCreate({"name": "string"})
topic.create_topic(db, testTopic, _user.id)
# create a video
testVideo = schemas.VideoCreate()
video.create_video(db, testVideo)
# create a tutorial
testTutorial = schemas.TutorialCreate()
_tutorial = tutorial.create_tutorial(db, testTutorial, user_id=_user.id)
# create a vote [List]
testVote = schemas.VoteCreate()
vote.create_vote(db, vote=testVote, user_id=_user.id, tutorial_id=_tutorial.id)

"""
This is the concept I want to output if you want to get one or more Tutorials
{
    "id": 1,
    "name": string,
    "description": string,
    "topic": {
        "id": 2,
        "name": string
    },
    "level": 3,
    "votes": [
        {
            "id": 2,
            "up": true,
            "user_id": 2
        },
        {
            "id": 1,
            "up": false,
            "user_id": 4
        } 
    ],
    "videos": [
        {
            "id": 1,
            "name": string,
            "url": string,
            "user_id": 2
        }
    ]
    "creator": {
        "id": 3,
        "identification": string
    }
}
"""

if __name__ == '__main__':
    pass