from fastapi.testclient import TestClient
from main import app
from queries.playlists import PlaylistRepository

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_playlists(self):
        return []


def test_get_all_playlists():
    app.dependency_overrides[PlaylistRepository] = EmptyPlaylistQueries

    response = client.get("/playlists")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {"playlists": []}
