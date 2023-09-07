from fastapi.testclient import TestClient
from main import app
from queries.tracks import TrackRepository

client = TestClient(app)


class EmptyTrackQueries:
    def get_tracks(self):
        return []


def test_get_all_tracks():
    app.dependency_overrides[TrackRepository] = EmptyTrackQueries
    # Arrange

    # Act
    response = client.get("/tracks")

    app.dependency_overrides = {}

    # Assert
    assert response.status_code == 200
    assert response.json() == {"tracks": []}
