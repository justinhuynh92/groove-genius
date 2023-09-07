steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE users (
            id SERIAL PRIMARY KEY NOT NULL,
            username VARCHAR(20) NOT NULL UNIQUE,
            password TEXT NOT NULL
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
            genre VARCHAR(30) NOT NULL
        );

        CREATE TABLE playlists (
            name VARCHAR(30) NOT NULL,
            id SERIAL PRIMARY KEY NOT NULL
            );


        CREATE TABLE playlist_tracks (
        playlist_id INT NOT NULL REFERENCES playlists(id) ON DELETE CASCADE,
        track_id INT NOT NULL REFERENCES tracks(id),
        PRIMARY KEY (playlist_id, track_id)
        );

        """,
        # "Down" SQL statement
        """
        DROP TABLE playlist_tracks;
        DROP TABLE playlists;
        DROP TABLE tracks;
        DROP TABLE genres;
        DROP TABLE users;
        """,
    ],
]
