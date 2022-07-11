from fastapi.testclient import TestClient
from api.main import app
from fastapi import status
import pytest

client = TestClient(app)

app.name = "roman"
app.password = "test"
app.id: int = 0
app.token: str = ""


def create(_name: str, _password: str):
    return client.post("/user/", json={"identification": _name, "password": _password})

@pytest.mark.parametrize("name, password,expected", [
    ('roman', 'test', status.HTTP_200_OK),
    ('roman', 'test', status.HTTP_400_BAD_REQUEST),
])
def test_multi_create(name, password, expected):
    response = create(name, password)
    response_json = response.json()
    app.id = response_json.get("id")
    print(response.json())
    assert response.status_code == expected

def test_login():
    response = client.post("/login", headers={"accept": "application/json","Content-Type": "application/x-www-form-urlencoded"}, data=f"username={app.name}&password={app.password}&scope=&client_id=&client_secret=")
    app.token = response.json().get("access_token")
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.parametrize("name,header,expected", [
    ('jan', True, status.HTTP_200_OK),
    ('test', True, status.HTTP_200_OK),
    ('jan', False, status.HTTP_401_UNAUTHORIZED),
    ('janzi', True, status.HTTP_200_OK),
])
def test_search_identity(name, header, expected):
    if header:
        response = client.get(f"/user/?identification={name}", headers={"Authorization": f"Bearer {app.token}"})
    else:
        response = client.get(f"/user/?identification={name}")
    print(response.json())
    assert response.status_code == expected
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

def test_login_second():
    response = client.post("/login", headers={"accept": "application/json","Content-Type": "application/x-www-form-urlencoded"}, data=f"username={app.name}&password={app.password}&scope=&client_id=&client_secret=")
    app.token = response.json().get("access_token")
    assert response.status_code == status.HTTP_200_OK

def test_search_id_failed():
    response = client.get(f"/user/?id={app.id}", headers={"Authorization": f"Bearer {app.token}"})
    print(response.json())
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json().get("identification") == app.name
