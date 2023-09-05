from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository
from models.users import UserOut

client = TestClient(app)

class UserRepo:
    def get_user(self, userID: str):
        return UserOut(
            userId=str,
        )

def test_get_user():
    app.dependency_overrides[UserRepository] = UserRepo
    response = client.get("/users")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == []
