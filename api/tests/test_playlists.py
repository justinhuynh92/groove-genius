from fastapi.testclient import TestClient
from main import app
from queries.playlists import PlaylistRepository

client = TestClient(app)


class EmptyPlaylistQueries:
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

    def test_get_single_playlist():
        # Override the real dependency with the mock
        app.dependency_overrides[PlaylistRepository] = EmptyPlaylistQueries

        # Perform the test request
        response = client.get("/playlists/1")

        # Assertions to make sure you're getting what you expect
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
