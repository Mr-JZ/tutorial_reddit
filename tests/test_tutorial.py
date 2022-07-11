import asyncio

import pytest
from fastapi import status
from fastapi.testclient import TestClient
from api.main import app
import test_user

client = TestClient(app)

app.name: str = "janzi"
app.password: str = "test"
app.id: int = 0


@pytest.mark.parametrize("json_input,expected", [
    ({"name": "test tutorial", "level": 0, "topic_id": 0, "description": "This is a smal test"}, status.HTTP_200_OK)
])
def test_create(json_input, expected, login_token):
    response = client.post("/tutorial/", headers={"Authorization": f"Bearer {login_token.__await__()}"}, json=json_input)
    print(response.json())
    response_json = response.json()
    app.id = response_json.get("id")
    assert response.status_code == expected


def test_search_identity(login_token):
    response = client.get(f"/user/?identification={app.name}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    response = client.get(f"/user/?identification={app.name}", headers={"Authorization": f"Bearer {login_token}"})
    assert response.status_code == status.HTTP_200_OK
    app.id = response.json().get("id")


def test_search_id(login_token):
    response = client.get(f"/user/?id={app.id}", headers={"Authorization": f"Bearer {login_token}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("identification") == app.name


def test_delete(login_token):
    response = client.delete(f"/user/?user_id={app.id}", headers={"Authorization": f"Bearer {login_token}"})
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    test_user.delete()
