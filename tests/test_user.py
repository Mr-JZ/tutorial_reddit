from fastapi.testclient import TestClient
from api.main import app
from fastapi import status

client = TestClient(app)

app.name: str = "janzi"
app.password: str = "test"
app.id: int = 0
app.token: str = ""

def create(_name: str, _password: str):
    return client.post("/user/", json={"identification": _name, "password": _password})

def test_create():
    response = create(app.name, app.password)
    response_json = response.json()
    app.id = response_json.get("id")
    print(response.json())
    assert response.status_code == status.HTTP_200_OK

def test_create_again():
    response = create(app.name, app.password)
    print(response.json())
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_login():
    response = client.post("/login", headers={"accept": "application/json","Content-Type": "application/x-www-form-urlencoded"}, data=f"username={app.name}&password={app.password}&scope=&client_id=&client_secret=")
    app.token  = response.json().get("access_token")
    assert response.status_code == status.HTTP_200_OK

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

def delete():
    return client.delete(f"/user/?user_id={app.id}", headers={"Authorization": f"Bearer {app.token}"})

def test_delete():
    response = delete()
    print(response.json())
    assert response.status_code == status.HTTP_200_OK


