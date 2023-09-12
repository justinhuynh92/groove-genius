from fastapi.testclient import TestClient
from main import app
from queries.playlists import PlaylistRepository

client = TestClient(app)


class EmptyPlaylistQueries:
    def get_playlists(self):
        return []

    def get_playlist(self, id: int):
        return {
            "id": 1,
            "name": "string",
            "tracks": [
                {
                    "id": 1,
                    "title": "string",
                    "artist": "string",
                    "album": "string",
                    "genre": "ROCK",
                },
                {
                    "id": 2,
                    "title": "string",
                    "artist": "string",
                    "album": "string",
                    "genre": "ROCK",
                },
            ],
        }


def test_get_all_playlists():
    app.dependency_overrides[PlaylistRepository] = EmptyPlaylistQueries

    response = client.get("/playlists/1")

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "string",
        "tracks": [
            {
                "id": 1,
                "title": "string",
                "artist": "string",
                "album": "string",
                "genre": "ROCK",
            },
            {
                "id": 2,
                "title": "string",
                "artist": "string",
                "album": "string",
                "genre": "ROCK",
            },
        ],
    }
