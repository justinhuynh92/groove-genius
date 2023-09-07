from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository
from models.users import UserOut

client = TestClient(app)

class UserRepo:
    def get_user(self, username: str):
        mock_user_data = UserOut(userId=1, username=username)
        return mock_user_data

def test_get_users():
    app.dependency_overrides[UserRepository] = UserRepo
    response = client.get("/users/{id}")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {"userId": 1}
