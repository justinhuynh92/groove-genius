from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository
from pydantic import BaseModel
from authenticator import authenticator

client = TestClient(app)

class UserOut(BaseModel):
    userId: str

class MockUserRepo:
    def get_user(self):
        return [{"userId": 1}]

def mock_get_user():
    return UserOut(userId=1)

def test_get_user():
    app.dependency_overrides[authenticator.get_current_account_data] = mock_get_user
    app.dependency_overrides[UserRepository] = MockUserRepo
    response = client.get("/users")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == [{"userId": 1}]

def test_init():
    assert 1 == 1
