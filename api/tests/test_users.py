from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository

client = TestClient(app)


class UserRepo:
    def get_user(self, userID: int):
        return None


def test_get_users():
    app.dependency_overrides[UserRepository] = UserRepo
    response = client.get("/accounts")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() is None


def test_init():
    assert 1 == 1
