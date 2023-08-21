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
            name VARCHAR(30) NOT NULL,
            id SERIAL PRIMARY KEY NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE users;
        DROP TABLE genres;
        """,
    ],
]
