from fastapi.testclient import TestClient
from main import app
from queries.users import UserRepository
from models.users import UserOut

client = TestClient(app)

class MockUserRepo:
    def get_user(self, userID: str):
        return UserOut(
            userId=str,
        )

def test_get_user():
    app.dependency_overrides[UserRepository] = MockUserRepo
    response = client.get("/users/{id}")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {
        "userId": str,
        }
