from fastapi.testclient import TestClient
from main import app
from queries.tracks import TrackRepository

client = TestClient(app)


class EmptyTrackQueries:

    def get_track_by_id(self, track_id: int):
        return {
            "id": 1,
            "title": "string",
            "artist": "string",
            "album": "string",
            "genre": "ROCK"
        }

    def test_get_track_by_id():
        app.dependency_overrides[TrackRepository] = EmptyTrackQueries
        # Arrange

        # Act
        response = client.get("/tracks/1")

        app.dependency_overrides = {}

        # Assert
        assert response.status_code == 200
        assert response.json() == {
            "id": 1,
            "title": "string",
            "artist": "string",
            "album": "string",
            "genre": "ROCK"
        }
