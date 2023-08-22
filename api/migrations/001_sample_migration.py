steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(20) NOT NULL,
            password VARCHAR(20) NOT NULL
        );

        CREATE TABLE genres (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(30) NOT NULL
        );

         CREATE TABLE tracks (
            id SERIAL PRIMARY KEY NOT NULL,
            title VARCHAR(20) NOT NULL,
            artist VARCHAR(20) NOT NULL,
            album VARCHAR(30) NOT NULL,
            genre_id INT NOT NULL
        );

        CREATE TABLE playlists (
            name VARCHAR(30) NOT NULL,
            id SERIAL PRIMARY KEY NOT NULL,
            user_id INT NOT NULL REFERENCES users(id)
            );

        CREATE TABLE track_genres (
        track_id INT NOT NULL REFERENCES tracks(id),
        genre_id INT NOT NULL REFERENCES genres(id)
        );

        CREATE TABLE user_playlists (
        user_id INT NOT NULL REFERENCES users(id),
        playlist_id INT NOT NULL REFERENCES playlists(id)
        );

        CREATE TABLE playlist_tracks (
        playlist_id INT NOT NULL REFERENCES playlists(id),
        track_id INT NOT NULL REFERENCES tracks(id)
        );

        """,
        # "Down" SQL statement
        """
        DROP TABLE track_genres;
        DROP TABLE playlist_tracks;
        DROP TABLE user_playlists;
        DROP TABLE playlists;
        DROP TABLE tracks;
        DROP TABLE genres;
        DROP TABLE users;
        """,
    ],
]
