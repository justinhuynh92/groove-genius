from fastapi.testclient import TestClient
from main import app
from queries.genres import GenreRepository

client = TestClient(app)


class EmptyGenre:
    def get_all(self):
        return []


def test_get_all_genres():
    app.dependency_overrides[GenreRepository] = EmptyGenre

    response = client.get("/genres")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == []
