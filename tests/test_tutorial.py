import asyncio

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from api.main import app
import test_user

client = TestClient(app)

app.name: str = "janzi"
app.password: str = "test"
app.token: str = test_user.test_login()
app.id : int = 0


@pytest.mark.parametrize("json_input,expected", [
    ({"name": "test tutorial", "level": 0, "topic_id": 0, "description": "This is a smal test"}, status.HTTP_200_OK)
])
def test_create(json_input, expected):
    response = client.post("/tutorial/", headers={"Authorization": f"Bearer {app.token}"}, params=json_input)
    print(response.json())
    app.id = response.json().get("id")
    assert response.status_code == expected


def test_get():
    response = client.get(f"/tutorial?id=1")
    print(response.json())


def test_search_id(login_token):
    response = client.get(f"/user/?id={app.id}", headers={"Authorization": f"Bearer {login_token}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("identification") == app.name


def test_delete(login_token):
    response = client.delete(f"/user/?user_id={app.id}", headers={"Authorization": f"Bearer {login_token}"})
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    test_user.delete()
