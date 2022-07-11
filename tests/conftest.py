import pytest
from api.main import app
from tests import test_user
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture(scope="function")
def login_token():
    name = "janzi"
    password = "test"
    response = test_user.create(name, password)
    app.id = response.json().get("id")
    response = client.post("/login",
                           headers={"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"},
                           data=f"username={name}&password={password}&scope=&client_id=&client_secret=")
    return response.json().get("access_token")

