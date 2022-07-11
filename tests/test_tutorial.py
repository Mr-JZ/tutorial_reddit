from fastapi import status
from fastapi.testclient import TestClient
from src.api.main import app
import test_user

client = TestClient(app)

app.name: str = "janzi"
app.password: str = "test"
app.id: int = 0
app.token: str = ""

def test_login():
    response = test_user.create(app.name, app.password)
    app.id = response.json().get("id")
    response = client.post("/login", headers={"accept": "application/json","Content-Type": "application/x-www-form-urlencoded"}, data=f"username={app.name}&password={app.password}&scope=&client_id=&client_secret=")
    app.token  = response.json().get("access_token")
    assert response.status_code == status.HTTP_200_OK

def test_create():
    response = client.post("/tutorial/", headers={"Authorization": f"Bearer {app.token}"})
    print(response.json())
    response_json = response.json()
    app.id = response_json.get("id")
    assert response.status_code == status.HTTP_200_OK

def test_create_again():
    response = client.post("/tutorial/", headers={"Authorization": f"Bearer {app.token}"})
    print(response.json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_search_identity():
    response = client.get(f"/user/?identification={app.name}")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    response = client.get(f"/user/?identification={app.name}", headers={"Authorization": f"Bearer {app.token}"})
    assert response.status_code == status.HTTP_200_OK
    app.id = response.json().get("id")

def test_search_id():
    response = client.get(f"/user/?id={app.id}", headers={"Authorization": f"Bearer {app.token}"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json().get("identification") == app.name

def test_delete():
    response = client.delete(f"/user/?user_id={app.id}", headers={"Authorization": f"Bearer {app.token}"})
    print(response.json())
    assert response.status_code == status.HTTP_200_OK
    test_user.delete()
